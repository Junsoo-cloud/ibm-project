import os
from dotenv import load_dotenv
import re
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from prompt_template_en import generate_prompt

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
def create_prompt(age, gender, hr, incline, experience):
    return generate_prompt(age, gender, hr, incline, experience)

# 프롬프트를 직접 문자열로 생성합니다.
prompt = create_prompt(30, "male", 200, 4, "Intermediate")
# print(prompt)
def send_to_watsonxai(prompt,
                      model_name="meta-llama/llama-2-70b-chat",
                      decoding_method="greedy",
                      max_new_tokens=1000,
                      min_new_tokens=30,
                      temperature=0.7,
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

# model_id
FLAN_T5_XXL = 'google/flan-t5-xxl'
FLAN_UL2 = 'google/flan-ul2'
GPT_NEOX = 'eleutherai/gpt-neox-20b'
GRANITE_13B_CHAT = 'ibm/granite-13b-chat-v1'
GRANITE_13B_INSTRUCT = 'ibm/granite-13b-instruct-v1'
LLAMA_2_70B_CHAT = 'meta-llama/llama-2-70b-chat'
LLAMA_3_70B_INSTRUCT="meta-llama/llama-3-70b-instruct"
MPT_7B_INSTRUCT2 = 'ibm/mpt-7b-instruct2'
MT0_XXL = 'bigscience/mt0-xxl'
STARCODER = 'bigcode/starcoder'
MISTRAL_LARGE = "mistralai/mistral-large"

# Watsonx AI에 프롬프트 전송 및 응답 받기
response = send_to_watsonxai(prompt, model_name="meta-llama/llama-3-70b-instruct-batch")
# print(f"type: {type(response)}") type check
# print(response)
# 응답 출력 및 디버깅 정보
if isinstance(response, str) and len(response) > 0:
    # 정규 표현식으로 응답에서 원하는 패턴 추출
    filtered_response = re.search(r'(Maintain Pace|Increase Pace|Decrease Pace)', response.strip())
    if filtered_response:
        print(filtered_response.group())
    else:
        print("No valid response received.")
else:
    print("Response is empty or not a string.")
