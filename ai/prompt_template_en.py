# prompt_template.py

def generate_prompt(age, gender, hr, incline, experience):
    prompt_template = f"""
    instruction: |
        1. For the given individual, determine the optimal running pace by considering the following factors and respond with one of the options: [maintain pace, increase pace, decrease pace]. 
    Do not include any other explanations, code, or calculation results. Before answering, think logically based on the provided information and respond accordingly.
        2. Since you cannot change the running incline, consider it when providing your response.

    context: |
    To maintain the optimal running pace, consider the following closely:
    [Age, Heart Rate, Running Incline, Running Experience Level (Beginner/Intermediate/Advanced)]

    - Heart Rate
        Maximum Heart Rate Calculation:
        Maximum heart rate varies by age and is generally calculated using the following formula:
        Maximum Heart Rate = 220 - Age
        If the current heart rate exceeds the maximum heart rate, respond with 'Decrease Pace'.

        Heart Rate Zones During Running:
        Heart rate can generally be divided into the following zones:

        Low Heart Rate (Walking Level): 50-60% of Maximum Heart Rate or lower
        Moderate Heart Rate (Aerobic Exercise, Normal Running Level): 60-80% of Maximum Heart Rate
        High Heart Rate (High-Intensity Exercise, Fast Running Level): 80-90% or more of Maximum Heart Rate

        20s: Maximum Heart Rate about 200 bpm, Moderate Heart Rate 120-160 bpm, High Heart Rate 160-180 bpm.
        30s: Maximum Heart Rate about 190 bpm, Moderate Heart Rate 114-152 bpm, High Heart Rate 152-171 bpm.
        40s: Maximum Heart Rate about 180 bpm, Moderate Heart Rate 108-144 bpm, High Heart Rate 144-162 bpm.
        50s: Maximum Heart Rate about 170 bpm, Moderate Heart Rate 102-136 bpm, High Heart Rate 136-153 bpm.
        60s: Maximum Heart Rate about 160 bpm, Moderate Heart Rate 96-128 bpm, High Heart Rate 128-144 bpm.

        Low Heart Rate Zone: If capable, suggest increasing the pace slightly to reach an effective training zone.
        Moderate Heart Rate Zone: Recommend maintaining the current pace to effectively improve cardiovascular health and endurance.
        High Heart Rate Zone: Recommend decreasing the pace to prevent excessive fatigue.

        Adjustment by Experience Level: Provide responses tailored to beginners, intermediate, or advanced runners.

    - Incline
        Heart Rate and Incline Assessment:

        Evaluate exercise intensity based on the current heart rate and incline. If the incline is high and the heart rate is elevated, the exercise intensity may be too high.
        When the heart rate is high, consider adjusting the pace based on the incline.

        Incline Zones Definition:
        Low Incline (0-3 degrees):

        Description: Close to flat terrain with relatively low burden during running. This is the most common incline experienced in general running situations.
        Recommended Pace Adjustment: With a low incline, adjusting the heart rate and pace is relatively flexible. Suitable for running at a faster pace or covering a target distance quickly.
        Moderate Incline (4-7 degrees):

        Description: Slight incline increases exercise intensity to a moderate level. There may be some level of burden depending on fitness.
        Recommended Pace Adjustment: With a moderate incline, it is advisable to maintain the heart rate in the moderate range. Adjust the pace to control the intensity of the exercise and avoid excessively high heart rates if needed.
        High Incline (8 degrees or more):

        Description: Steep incline significantly increases exercise intensity. Heart rate may rise quickly, and physical exertion increases.
        Recommended Pace Adjustment: When the incline is high, heart rate may rise rapidly, so it is advisable to reduce the pace and lower the intensity of the exercise. Periodic rest and heart rate control are needed at high inclines, and long periods of exercise at very steep inclines should be avoided.

        Responses Based on Incline:
        Low Incline (0-3 degrees):
        Pace: It is fine to maintain or slightly increase the pace.
        Heart Rate: Adjust within a suitable range and maintain stable exercise.
        Additional Tip: Maintain the usual running pace without special adjustments.
        
        Moderate Incline (4-7 degrees):
        Pace: Adjust to a moderate level to maintain exercise intensity appropriately.
        Heart Rate: Watch to ensure heart rate does not become too high and adjust pace if necessary.
        Additional Tip: Consider periodic rest to manage exercise intensity.
        
        High Incline (8 degrees or more):
        Pace: Recommend decreasing the pace.
        Heart Rate: To avoid rapid heart rate increases, adjust the pace to maintain heart rate within a safe range.

    Example 1:
    Input:
        Age: 25
        Gender: Female
        Current Heart Rate: 110 bpm
        Current Running Incline: 2 degrees
        Running Experience Level: Beginner
    Reasoning:
        1. The individual is 25 years old, so the maximum heart rate is about 195 bpm.
        2. The current heart rate of 110 bpm is about 56% of the maximum heart rate, which falls into the low heart rate zone.
        3. An incline of 2 degrees is low, so the exercise intensity is low.
        4. As a beginner, it is better to maintain a stable pace rather than increasing intensity.
    Output:
        Maintain Pace

    Example 2:
    Input:
        Age: 35
        Gender: Male
        Current Heart Rate: 145 bpm
        Current Running Incline: 6 degrees
        Running Experience Level: Intermediate
    Reasoning:
        1. The individual is 35 years old, so the maximum heart rate is about 185 bpm.
        2. The current heart rate of 145 bpm is about 78% of the maximum heart rate, which falls into the moderate heart rate zone.
        3. An incline of 6 degrees is moderate, so the exercise intensity is medium.
        4. For an intermediate runner, it is important to maintain an appropriate heart rate. However, due to the incline, the heart rate is somewhat high, so decreasing the pace is advisable.
    Output:
        Decrease Pace

    Example 3:
    Input:
        Age: 40
        Gender: Female
        Current Heart Rate: 130 bpm
        Current Running Incline: 4 degrees
        Running Experience Level: Advanced
    Reasoning:
        1. The individual is 40 years old, so the maximum heart rate is about 180 bpm.
        2. The current heart rate of 130 bpm is about 72% of the maximum heart rate, which falls into the moderate heart rate zone.
        3. An incline of 4 degrees is moderate, so the exercise intensity is medium.
        4. As an advanced runner, they can handle higher heart rates, so maintaining the current pace is appropriate.
    Output:
        Maintain Pace

    Example 4:
    Input:
        Age: 50
        Gender: Male
        Current Heart Rate: 160 bpm
        Current Running Incline: 8 degrees
        Running Experience Level: Beginner
    Reasoning:
        1. The individual is 50 years old, so the maximum heart rate is about 170 bpm.
        2. The current heart rate of 160 bpm is about 94% of the maximum heart rate, which falls into the high heart rate zone.
        3. An incline of 8 degrees is high, so the exercise intensity is significantly increased.
        4. As a beginner, adapting to high inclines and high heart rates may be challenging, so decreasing the pace is necessary.
    Output:
        Decrease Pace

    Example 5:
    Input:
        Age: 45
        Gender: Female
        Current Heart Rate: 120 bpm
        Current Running Incline: 3 degrees
        Running Experience Level: Intermediate
    Reasoning:
        1. The individual is 45 years old, so the maximum heart rate is about 175 bpm.
        2. The current heart rate of 120 bpm is about 69% of the maximum heart rate, which falls into the moderate heart rate zone.
        3. An incline of 3 degrees is low, so the exercise intensity is low.
        4. For an intermediate runner, maintaining an appropriate heart rate is beneficial, so maintaining the current pace is appropriate.
    Output:
        Maintain Pace

    input: |
    Given the following conditions: 
        Person:
        Age: {age}
        Gender: {gender}
        Current Heart Rate: {hr} bpm
        Current Running Incline: {incline} degrees
        Running Experience Level: {experience}
    """
    return prompt_template
