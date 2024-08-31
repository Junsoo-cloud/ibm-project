# prompt_template.py

def generate_prompt(age, gender, hr, incline, experience):
    prompt_template = f"""
    instruction: |
        1. 주어진 사람에 대해서 최적의 러닝 페이스를 유지할 수 있도록 아래 요소들을 고려하여 러닝 페이스에 대해 오직 [페이스 유지, 페이스 올림, 페이스 낮춤] 셋 중 하나로 대답해주세요. 
    그 외의 다른 설명이나 코드, 계산 결과를 포함하지 마세요. 답변하기 전에, 주어진 정보를 바탕으로 논리적인 사고 과정을 생각하고 답변하세요.
        2. 러닝 경사는 당신이 바꿀 수 없으니 이를 고려하여 답변하세요.

    context: |
    최적의 러닝 페이스를 유지하기 위해서는 다음과 같은 요소들을 밀접하게 고려해봐야 해:
    [나이, 심박수, 러닝 경사, 러닝[초보자/중급자/상급자]]

    - 심박수
        최대 심박수 계산:
        최대 심박수는 나이에 따라 달라지며, 일반적으로 다음 공식을 사용해 계산합니다.
        최대 심박수는 220 - 나이
        만약 현재의 심박수가 최대 심박수보다 높을 시 , 무조건 '페이스 낮춤' 으로 답변합니다.

        러닝 중 심박수 구간:
        심박수는 일반적으로 다음과 같은 구간으로 나눌 수 있습니다:

        낮은 심박수 (걷기 수준): 최대 심박수의 50-60% 이하
        적당한 심박수 (유산소 운동, 보통 러닝 수준): 최대 심박수의 60-80%
        높은 심박수 (고강도 운동, 빠른 러닝 수준): 최대 심박수의 80-90% 이상

        20대: 최대 심박수 약 200 bpm, 적당한 심박수는 120-160 bpm, 높은 심박수는 160-180 bpm.
        30대: 최대 심박수 약 190 bpm, 적당한 심박수는 114-152 bpm, 높은 심박수는 152-171 bpm.
        40대: 최대 심박수 약 180 bpm, 적당한 심박수는 108-144 bpm, 높은 심박수는 144-162 bpm.
        50대: 최대 심박수 약 170 bpm, 적당한 심박수는 102-136 bpm, 높은 심박수는 136-153 bpm.
        60대: 최대 심박수 약 160 bpm, 적당한 심박수는 96-128 bpm, 높은 심박수는 128-144 bpm.

        낮은 심박수 구간: 사용자가 능력이 된다면 효과적인 훈련 구간에 도달하기 위해 페이스를 적당히 높일 것을 제안합니다.
        적당한 심박수 구간: 현재 페이스를 유지하면서 심혈관 건강과 지구력을 효과적으로 키울 수 있도록 권장합니다.
        높은 심박수 구간: 과도한 피로를 방지하기 위해 페이스를 줄일 것을 권장합니다. 

        경험 수준에 따른 조정: 초보자, 중급자, 고급자에 따라 맞춤형으로 답변을 제공합니다.

    - 경사
        심박수와 경사 평가:

        현재 심박수와 경사를 고려하여 운동 강도를 평가합니다. 높은 경사에서 심박수가 높아지면 운동 강도가 과도할 수 있습니다.
        심박수가 높은 구간에 있을 때 경사가 높으면, 운동의 부담이 커질 수 있으니 이를 반영하여 페이스를 조정합니다.

        경사의 구간 정의:
        낮은 경사 (0-3도):

        설명: 평지에 가까운 수준으로, 러닝 시 부담이 상대적으로 적습니다. 일반적인 러닝 상황에서 가장 자주 경험하는 경사입니다.
        추천 페이스 조정: 경사가 낮으므로 심박수와 페이스 조정이 비교적 자유롭습니다. 러닝 페이스를 빠르게 하거나 목표 거리를 빠르게 소화하는 데 적합합니다.
        적당한 경사 (4-7도):

        설명: 약간의 경사로 인해 운동 강도가 중간 정도로 증가합니다. 체력에 따라 어느 정도의 부담이 있을 수 있습니다.
        추천 페이스 조정: 경사가 적당하므로 심박수를 중간 범위에서 유지하는 것이 좋습니다. 페이스를 적절히 조절하여 운동의 강도를 조절합니다. 너무 높은 심박수를 피하며, 필요한 경우 페이스를 조정할 수 있습니다.
        높은 경사 (8도 이상):

        설명: 상당히 가파른 경사로, 운동 강도가 크게 증가합니다. 심박수가 빠르게 상승할 수 있으며, 체력 소모가 커집니다.
        추천 페이스 조정: 경사가 높을 때는 심박수가 급격히 상승할 수 있으므로, 페이스를 줄이고 운동 강도를 낮추는 것이 좋습니다. 높은 경사에서는 주기적인 휴식과 심박수 조절이 필요하며, 너무 높은 경사에서의 장시간 운동은 피하는 것이 바람직합니다.

        경사에 따른 답변:
        낮은 경사 (0-3도):
        페이스: 유지하거나 약간 빠르게 조정해도 좋습니다.
        심박수: 적당한 범위 내에서 조절하며, 안정적인 운동을 유지합니다.
        추가 팁: 특별한 조정 없이 평소의 러닝 페이스를 유지합니다.
        
        적당한 경사 (4-7도):
        페이스: 중간 정도로 조절하여 운동 강도를 적절히 유지합니다.
        심박수: 심박수가 너무 높아지지 않도록 주의하며, 페이스를 조정합니다.
        추가 팁: 주기적인 휴식을 고려하여 운동 강도를 조절합니다.
        
        높은 경사 (8도 이상):
        페이스: 페이스를 줄이는 것을 권장합니다.
        심박수: 심박수가 급격히 상승할 수 있으니, 높은 심박수를 방지하기 위해 페이스를 조절합니다.

    예제 1:
    Input:
        나이: 25
        성별: 여성
        현재 심박수: 110 bpm
        현재 러닝 경사: 2도
        러닝 경험 수준: 초보자
    Reasoning:
        1. 사용자의 나이는 25세로, 최대 심박수는 약 195 bpm입니다.
        2. 현재 심박수 110 bpm은 최대 심박수의 약 56%로, 낮은 심박수 범위에 해당합니다.
        3. 경사 2도는 낮은 경사로, 운동 강도가 적습니다.
        4. 초보자는 너무 높은 강도로 운동하기보다는 안정적인 페이스를 유지하는 것이 좋습니다.
    Output:
        페이스 유지

    예제 2:
    Input:
        나이: 35
        성별: 남성
        현재 심박수: 145 bpm
        현재 러닝 경사: 6도
        러닝 경험 수준: 중급자
    Reasoning:
        1. 사용자의 나이는 35세로, 최대 심박수는 약 185 bpm입니다.
        2. 현재 심박수 145 bpm은 최대 심박수의 약 78%로, 적당한 심박수 범위에 해당합니다.
        3. 경사 6도는 적당한 경사로, 운동 강도가 중간 정도입니다.
        4. 중급자는 일정 강도로 운동하며 심박수를 적당히 유지하는 것이 중요합니다. 그러나 경사로 인해 심박수가 다소 높아지므로 페이스를 낮추는 것이 좋습니다.
    Output:
        페이스 낮춤

    예제 3:
    Input:
        나이: 40
        성별: 여성
        현재 심박수: 130 bpm
        현재 러닝 경사: 4도
        러닝 경험 수준: 상급자
    Reasoning:
        1. 사용자의 나이는 40세로, 최대 심박수는 약 180 bpm입니다.
        2. 현재 심박수 130 bpm은 최대 심박수의 약 72%로, 적당한 심박수 범위에 해당합니다.
        3. 경사 4도는 적당한 경사로, 운동 강도가 중간 정도입니다.
        4. 상급자는 높은 심박수를 감당할 수 있으므로 현재 페이스를 유지하며 운동을 계속하는 것이 적절합니다.
    Output:
        페이스 유지

    예제 4:
    Input:
        나이: 50
        성별: 남성
        현재 심박수: 160 bpm
        현재 러닝 경사: 8도
        러닝 경험 수준: 초보자
    Reasoning:
        1. 사용자의 나이는 50세로, 최대 심박수는 약 170 bpm입니다.
        2. 현재 심박수 160 bpm은 최대 심박수의 약 94%로, 높은 심박수 범위에 해당합니다.
        3. 경사 8도는 높은 경사로, 운동 강도가 크게 증가합니다.
        4. 초보자는 높은 경사와 높은 심박수에 적응하기 어려울 수 있으므로, 페이스를 낮추는 것이 필요합니다.
    Output:
        페이스 낮춤

    예제 5:
    Input:
        나이: 45
        성별: 여성
        현재 심박수: 120 bpm
        현재 러닝 경사: 3도
        러닝 경험 수준: 중급자
    Reasoning:
        1. 사용자의 나이는 45세로, 최대 심박수는 약 175 bpm입니다.
        2. 현재 심박수 120 bpm은 최대 심박수의 약 69%로, 적당한 심박수 범위에 해당합니다.
        3. 경사 3도는 낮은 경사로, 운동 강도가 낮습니다.
        4. 중급자는 심박수를 적당히 유지하면서 운동하는 것이 좋으며, 현재 상황에서는 페이스를 유지하는 것이 적절합니다.
    Output:
        페이스 유지

    input: |
    Given the following conditions: 
        사람 :
        나이: {age}
        성별: {gender}
        현재 심박수: {hr} bpm
        현재 러닝 경사: {incline}도
        러닝 경험 수준: {experience}
    """
    return prompt_template
