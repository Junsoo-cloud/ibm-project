def generate_prompt(age, gender, hr, incline, experience, goal_distance, distance_covered):
    prompt_template = f"""
    instruction: |
        1. For the given person, provide a response on how to maintain the optimal running pace by choosing one of [Maintain Pace, Increase Pace, Decrease Pace]. Do not include any additional explanations, code, or calculation results. Before responding, think through the provided information and reasoning.
        2. Since you cannot change the running incline, consider it when making your response.
        3. Adjust the pace appropriately based on the goal distance, remaining distance, and distance already covered.
        4. If the current heart rate is higher than the maximum heart rate, answer with 'Decrease Pace' unconditionally.

    context: |
    To maintain the optimal running pace, consider the following closely:
    [Age, Heart Rate, Running Incline, Running Experience Level (Beginner/Intermediate/Advanced)]
    Consider the individual's fitness level and experience when adjusting the pace. If they are a beginner, prioritize safety and endurance over speed. For advanced runners, maintain a challenging but sustainable pace.
    - Heart Rate
        Maximum Heart Rate Calculation:
        Maximum heart rate varies with age and is generally calculated using the formula:
        Maximum Heart Rate = 220 - Age
        If the current heart rate is higher than the maximum heart rate, always respond with 'Decrease Pace'.

        Heart Rate Zones:
        Heart rates are typically divided into the following zones:

        Low Heart Rate (Walking level): Below 50-60% of Maximum Heart Rate
        Moderate Heart Rate (Aerobic exercise, moderate running level): 60-80% of Maximum Heart Rate
        High Heart Rate (High-intensity exercise, fast running level): Above 80-90% of Maximum Heart Rate

        20s: Maximum Heart Rate approximately 200 bpm, Moderate Heart Rate 120-160 bpm, High Heart Rate 160-180 bpm.
        30s: Maximum Heart Rate approximately 190 bpm, Moderate Heart Rate 114-152 bpm, High Heart Rate 152-171 bpm.
        40s: Maximum Heart Rate approximately 180 bpm, Moderate Heart Rate 108-144 bpm, High Heart Rate 144-162 bpm.
        50s: Maximum Heart Rate approximately 170 bpm, Moderate Heart Rate 102-136 bpm, High Heart Rate 136-153 bpm.
        60s: Maximum Heart Rate approximately 160 bpm, Moderate Heart Rate 96-128 bpm, High Heart Rate 128-144 bpm.

        Low Heart Rate Zone: If the user is capable, suggest increasing the pace to reach an effective training zone.
        Moderate Heart Rate Zone: Recommend maintaining the current pace to effectively build cardiovascular health and endurance.
        High Heart Rate Zone: Advise decreasing the pace to avoid excessive fatigue.

        Adjustment based on Experience Level: Provide tailored responses based on beginner, intermediate, or advanced levels.

    - Incline
        Heart Rate and Incline Assessment:

        Evaluate the exercise intensity considering the current heart rate and incline. A higher incline can lead to an increased heart rate and potentially excessive exercise intensity.
        When the heart rate is high and the incline is steep, the exercise burden can increase, so adjust the pace accordingly.

        Incline Zones:
        Low Incline (0-3 degrees):
        Description: Nearly flat, with relatively low running strain. It’s the most common incline in running situations.
        Recommended Pace Adjustment: With a low incline, pace and heart rate adjustments are more flexible. Suitable for increasing pace or achieving the goal distance more quickly.
        
        Moderate Incline (4-7 degrees):
        Description: Slight incline increases exercise intensity moderately. There may be some strain depending on fitness levels.
        Recommended Pace Adjustment: With a moderate incline, it’s best to maintain the heart rate within a moderate range. Adjust pace to manage exercise intensity and avoid excessive heart rates if needed.
        
        High Incline (8 degrees or more):
        Description: Steep incline significantly increases exercise intensity. The heart rate can rise quickly and the physical strain increases.
        Recommended Pace Adjustment: At high inclines, the heart rate can rise sharply, so it’s advisable to decrease the pace and lower the exercise intensity. High inclines may require periodic rest and heart rate management.

    - Goal Distance and Distance Covered
        Adjust the pace considering the goal distance and distance covered. 
        As the distance covered increases, fatigue also increases, so adjust the pace accordingly.

        Pace Adjustment Considering Goal Distance and Distance Covered:
        If the goal distance is far and the remaining distance is short, it may be appropriate to increase the pace, but adjust for fatigue as needed.
        Conversely, if the goal distance and remaining distance are close, maintaining or decreasing the pace might be appropriate.

    Example 1:
    Input:
        Age: 25
        Gender: Female
        Current Heart Rate: 110 bpm
        Current Running Incline: 2 degrees
        Running Experience Level: Beginner
        Goal Distance: 10 km
        Distance Covered: 2 km
    Reasoning:
        1. The user's age is 25, so the maximum heart rate is approximately 195 bpm.
        2. The current heart rate of 110 bpm is about 56% of the maximum heart rate, which falls into the low heart rate zone.
        3. The incline of 2 degrees is low, with minimal exercise strain.
        4. As a beginner, it is advisable to maintain a stable pace rather than increasing it.
        5. With 8 km remaining, it is appropriate to maintain the current pace.
    Output:
        Maintain Pace

    Example 2:
    Input:
        Age: 35
        Gender: Male
        Current Heart Rate: 145 bpm
        Current Running Incline: 6 degrees
        Running Experience Level: Intermediate
        Goal Distance: 10 km
        Distance Covered: 7 km
    Reasoning:
        1. The user's age is 35, so the maximum heart rate is approximately 185 bpm.
        2. The current heart rate of 145 bpm is about 78% of the maximum heart rate, which falls into the moderate heart rate zone.
        3. The incline of 6 degrees is moderate, with a moderate increase in exercise intensity.
        4. For an intermediate level, maintaining a steady intensity is important, but with 3 km remaining, increasing the pace may be beneficial.
    Output:
        Increase Pace

    Example 3:
    Input:
        Age: 40
        Gender: Female
        Current Heart Rate: 130 bpm
        Current Running Incline: 4 degrees
        Running Experience Level: Advanced
        Goal Distance: 15 km
        Distance Covered: 3 km
    Reasoning:
        1. The user's age is 40, so the maximum heart rate is approximately 180 bpm.
        2. The current heart rate of 130 bpm is about 72% of the maximum heart rate, which falls into the moderate heart rate zone.
        3. The incline of 4 degrees is moderate, with a moderate increase in exercise intensity.
        4. As an advanced runner, managing a higher heart rate is feasible, so maintaining the current pace is appropriate.
    Output:
        Maintain Pace

    Example 4:
    Input:
        Age: 50
        Gender: Male
        Current Heart Rate: 160 bpm
        Current Running Incline: 8 degrees
        Running Experience Level: Beginner
        Goal Distance: 5 km
        Distance Covered: 3 km
    Reasoning:
        1. The user's age is 50, so the maximum heart rate is approximately 170 bpm.
        2. The current heart rate of 160 bpm is about 94% of the maximum heart rate, which falls into the high heart rate zone.
        3. The incline of 8 degrees is high, significantly increasing exercise intensity.
        4. As a beginner, adapting to high incline and heart rate may be challenging, so decreasing the pace is recommended.
        5. With 2 km remaining, decreasing the pace to reduce fatigue and safely achieve the goal is advisable.
    Output:
        Decrease Pace

    Example 5:
    Input:
        Age: 45
        Gender: Female
        Current Heart Rate: 120 bpm
        Current Running Incline: 3 degrees
        Running Experience Level: Intermediate
        Goal Distance: 8 km
        Distance Covered: 4 km
    Reasoning:
        1. The user's age is 45, so the maximum heart rate is approximately 175 bpm.
        2. The current heart rate of 120 bpm is about 69% of the maximum heart rate, which falls into the moderate heart rate zone.
        3. The incline of 3 degrees is low, with minimal exercise strain.
        4. For an intermediate runner, maintaining or slightly increasing the pace may be appropriate, as the distance covered is half of the goal.
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
        Goal Distance: {goal_distance} km
        Distance Covered: {distance_covered} km
        Remaining Distance: {goal_distance - distance_covered} km
    """
    return prompt_template
