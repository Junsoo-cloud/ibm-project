import os
from dotenv import load_dotenv
import re
import yaml
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from prompt_template import generate_prompt

# 환경 변수 로드
load_dotenv()

# 환경 변수 가져오기
apikey = os.getenv('API_KEY')
project_id = os.getenv('PROJECT_ID')

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": apikey
}

print(f"Credentials: {credentials}")
print(f"Project ID: {project_id}")

# 프롬프트 생성
prompt = generate_prompt()

# 프롬프트를 파일로 저장합니다.
with open('prompt.yaml', 'w', encoding='utf-8') as file:
    file.write(prompt)

# print("Generated prompt.yaml:")
# print(prompt)

def send_to_watsonxai(prompts,
                      model_name="meta-llama/llama-2-70b-chat",
                      decoding_method="greedy",
                      max_new_tokens=1000,
                      min_new_tokens=30,
                      temperature=0.7,
                      repetition_penalty=1.2):
    '''
    프롬프트 및 매개 변수를 watsonx.ai로 보내기 위한 function
    
    Args:  
        prompts: 텍스트 프롬프트
        decoding_method: "sample" or "greedy"
        max_new_token:int watsonx.ai parameter for max new tokens/response returned
        temperature:float watsonx.ai parameter for temperature (range 0>2)
        repetition_penalty:float watsonx.ai parameter for repetition penalty (range 1.0 to 2.0)

    Returns: None
        prints response
    '''
    assert not any(map(lambda prompt: len(prompt) < 1, prompts)), "make sure none of the prompts in the inputs prompts are empty"

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

    response = model.generate_text(prompt=prompts)

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
# YAML 파일에서 프롬프트 읽기
with open('prompt.yaml', 'r', encoding='utf-8') as file:
    prompt_data = yaml.safe_load(file)
instruction = prompt_data['instruction']
context = prompt_data['context']
input_data = prompt_data['input']
print(f"prompt_data: {input_data}")
prompt = f"{instruction}\n\n{context}\n\n{input_data}"
prompts = [prompt]

# Watsonx AI에 프롬프트 전송 및 응답 받기
response = send_to_watsonxai(prompts, model_name="mistralai/mistral-large")

# 응답 출력 및 디버깅 정보
# print("Response object type:", type(response))
# print("Response content:", response)

# 응답이 올바르게 반환되었는지 확인
if isinstance(response, list) and len(response) > 0:
    for idx, res in enumerate(response):
        filtered_response = re.search(r'(페이스 유지|페이스 올림|페이스 낮춤)', res.strip())
        if filtered_response:
            print(filtered_response.group())
else:
    print("No valid response received.")
