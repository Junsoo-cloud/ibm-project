from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import json
import os
from dotenv import load_dotenv
import re
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from prompt_template_en import generate_prompt
import sqlite3

app = FastAPI()

class RunningData(BaseModel):
    age: int
    gender: str
    heartRate: int
    incline: int
    experience: str
    goalDistance: int
    distanceCovered: int

# 환경 변수 로드
load_dotenv()

# 환경 변수 가져오기
apikey = os.getenv('API_KEY')
project_id = os.getenv('PROJECT_ID')

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": apikey
}

# 프롬프트 생성
def create_prompt(age, gender, hr, incline, experience, goal_distance, distance_covered):
    return generate_prompt(age, gender, hr, incline, experience, goal_distance, distance_covered)

def send_to_watsonxai(prompt,
                      model_name="meta-llama/llama-2-70b-chat",
                      decoding_method="greedy",
                      max_new_tokens=200,
                      min_new_tokens=30,
                      temperature=0.2,
                      repetition_penalty=1.2):
    '''
    프롬프트 및 매개 변수를 watsonx.ai로 보내기 위한 function
    
    Args:  
        prompt: 텍스트 프롬프트
        decoding_method: "sample" or "greedy"
        max_new_token:int watsonx.ai parameter for max new tokens/response returned
        temperature:float watsonx.ai parameter for temperature (range 0>2)
        repetition_penalty:float watsonx.ai parameter for repetition penalty (range 1.0 to 2.0)

    Returns: None
        prints response
    '''
    assert len(prompt) > 0, "Prompt cannot be empty"

    # Instantiate parameters for text generation
    model_params = {
        GenParams.DECODING_METHOD: decoding_method,
        GenParams.MIN_NEW_TOKENS: min_new_tokens,
        GenParams.MAX_NEW_TOKENS: max_new_tokens,
        GenParams.RANDOM_SEED: 42,
        GenParams.TEMPERATURE: temperature,
        GenParams.REPETITION_PENALTY: repetition_penalty,
    }

    # Instantiate a model proxy object to send your requests
    model = Model(
        model_id=model_name,
        params=model_params,
        credentials=credentials,
        project_id=project_id)

    response = model.generate_text(prompt=prompt)

    return response

@app.post("/api/send-data")
async def send_data(data: RunningData):
    # 프롬프트 생성
    print(data)
    prompt = create_prompt(data.age, data.gender, data.heartRate, data.incline, data.experience, data.goalDistance, data.distanceCovered)
    
    # Watsonx AI에 프롬프트 전송 및 응답 받기
    response = send_to_watsonxai(prompt, model_name="meta-llama/llama-3-1-8b-instruct")
    
    result = response
    # # 응답 출력 및 디버깅 정보
    # if isinstance(response, str) and len(response) > 0:
    #     # 정규 표현식으로 응답에서 원하는 패턴 추출
    #     filtered_response = re.search(r'(Maintain Pace|Increase Pace|Decrease Pace)', response.strip())
    #     if filtered_response:
    #         result = filtered_response.group()
    #     else:
    #         result = "No valid response received."
    # else:
    #     result = "Response is empty or not a string."

    # SQLite3에 저장
    # running_data = {
    #     "age": data.age,
    #     "gender": data.gender,
    #     "heartRate": data.heartRate,
    #     "incline": data.incline,
    #     "experience": data.experience,
    #     "goalDistance": data.goalDistance,
    #     "distanceCovered": data.distanceCovered,
    #     "result": result
    # }

    conn = sqlite3.connect('running_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS running_data
                 (age INTEGER, gender TEXT, heartRate INTEGER, incline INTEGER, experience TEXT, goalDistance INTEGER, distanceCovered INTEGER, result TEXT)''')
    c.execute("INSERT INTO running_data (age, gender, heartRate, incline, experience, goalDistance, distanceCovered, result) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (data.age, data.gender, data.heartRate, data.incline, data.experience, data.goalDistance, data.distanceCovered, result))
    conn.commit()
    conn.close()

    return {"result": result}
