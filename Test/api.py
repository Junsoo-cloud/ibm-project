import requests
import json
import random
import time

# 난수 생성 시드를 설정 (결과를 재현 가능하게 하기 위해)
random.seed(42)

# 데이터 생성 함수
def generate_fake_data():
    return {
        "age": random.randint(18, 65),
        "gender": random.choice(["male", "female"]),
        "heartRate": random.randint(60, 180),
        "incline": random.randint(0, 15),
        "experience": random.choice(["beginner", "intermediate", "advanced"]),
        "goalDistance": random.uniform(5.0, 20.0),
        "distanceCovered": random.uniform(0.0, 15.0)
    }

# 30개의 가짜 데이터 생성
fake_data_list = [generate_fake_data() for _ in range(30)]

# 결과를 JSON 형식으로 변환
fake_data_json = json.dumps(fake_data_list, indent=2)

# 출력
print(fake_data_json)

def send_fakedata_to_server():
    url = "http://localhost:8000/api/health-data/"  # 서버의 API 엔드포인트
    headers = {"Content-Type": "application/json"}
    
    # 각 데이터 항목을 10초 간격으로 전송
    for data in fake_data_list:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            print("Data sent successfully")
            print("Response:", response.json())
        else:
            print("Failed to send data")
            print("Response:", response.status_code, response.text)
        
        # 10초 대기
        time.sleep(10)

if __name__ == "__main__":
    send_fakedata_to_server()
