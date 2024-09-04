import os
from dotenv import load_dotenv
import re
import json
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from prompt_template import generate_prompt
from prompt_feedback import generate_analysis_feedback_prompt

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
def create_prompt(age, gender, heart_rate, incline, experience, goal_distance, distance_covered):
    return generate_prompt(age, gender, heart_rate, incline, experience, goal_distance, distance_covered)

model = 'bigscience/mt0-xxl', 'codellama/codellama-34b-instruct-hf', 'google/flan-t5-xl', 'google/flan-t5-xxl', 
'google/flan-ul2', 'ibm/granite-13b-chat-v2', 'ibm/granite-13b-instruct-v2', 'ibm/granite-20b-code-instruct', 
'ibm/granite-20b-multilingual', 'ibm/granite-34b-code-instruct', 'ibm/granite-3b-code-instruct', 'ibm/granite-7b-lab',
'ibm/granite-8b-code-instruct', 'ibm/slate-125m-english-rtrvr', 'ibm/slate-125m-english-rtrvr-v2', 'ibm/slate-30m-english-rtrvr', 
'ibm/slate-30m-english-rtrvr-v2', 'intfloat/multilingual-e5-large', 'meta-llama/llama-2-13b-chat', 'meta-llama/llama-2-70b-chat',
'meta-llama/llama-3-1-70b-instruct', 'meta-llama/llama-3-1-8b-instruct', 'meta-llama/llama-3-405b-instruct',
'meta-llama/llama-3-70b-instruct', 'meta-llama/llama-3-70b-instruct-batch', 'meta-llama/llama-3-8b-instruct', 
'mistralai/mistral-large', 'mistralai/mixtral-8x7b-instruct-v01', 'sentence-transformers/all-minilm-l12-v2'

# 프롬프트를 직접 문자열로 생성합니다.
prompt = generate_prompt(60, "male", 51, 40, 4, "Intermediate", 10, 7)
print(prompt)
def send_to_watsonxai(prompt,
                      model_name,
                      decoding_method="greedy",
                      max_new_tokens=300,
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

# Watsonx AI에 프롬프트 전송 및 응답 받기
former_response = False
response = send_to_watsonxai(prompt, model_name="meta-llama/llama-3-70b-instruct")
# print(f"type: {type(response)}") type check
print(response)
# 응답 출력 및 디버깅 정보
if isinstance(response, str) and len(response) > 0:
    # 정규 표현식으로 응답에서 원하는 패턴 추출
    filtered_response = re.search(r'(Maintain Pace|Increase Pace|Decrease Pace)', response.strip())
    if filtered_response:
        if (filtered_response != former_response): # Different Response
            print(filtered_response.group())
            former_response = filtered_response
        else: # Same Response
            print('Same Pace') 
    else:
        print("No valid response received.")
else:
    print("Response is empty or not a string.")


def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


# feedback
json_file = 'sample_data.json'
json_data = read_json_file(json_file)

# 나머지 정보 정의
age = 30  # 예시 값, 실제로는 다른 소스에서 가져와야 함
gender = 'Male'  # 예시 값

# 피드백 프롬프트 생성

feedback_prompt = generate_analysis_feedback_prompt(age, gender, json_data)
response = send_to_watsonxai(feedback_prompt, model_name="meta-llama/llama-3-70b-instruct")

# validation check
if isinstance(response, str) and len(response) > 0:
    print(f"feedback : {response}")
else:
    print("Response is empty or not a string.")

