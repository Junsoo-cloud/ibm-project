def generate_analysis_feedback_prompt(age, gender, json_data):
    timestamp = json_data.get("timestamp", "")
    heart_rate = json_data.get("heartRate", 0)
    incline = json_data.get("incline", 0)
    distance_covered = json_data.get("distanceCovered", 0)
    vo2max = json_data.get("vo2max", 0)

    prompt_template = f"""
    instruction: |
        You are an AI designed to analyze running history and provide concise feedback to help improve future running sessions. Provide a one-line feedback on how the person can enhance their running experience. Include a separate section with the reasoning behind your feedback. Focus on actionable insights for improvement.

    context: |

    Analyze the running history and current data to provide feedback on improving future running sessions:
    [Age, Gender, Heart Rate, VO2 Max, Running Incline, Distance Covered]
    
    - Age
        Age affects endurance and recovery capacity. Consider how age impacts the individual's overall fitness and response to exercise.

    - Heart Rate
        Evaluate if the current heart rate falls into the low, moderate, or high heart rate zones. High heart rates may indicate overexertion, while low heart rates could suggest insufficient effort.
        
    - VO2 Max
        Analyze the VO2 Max to gauge aerobic capacity and endurance. Higher VO2 Max suggests better endurance, while lower VO2 Max indicates areas for improvement.

    - Incline
        Assess the impact of the incline on exercise intensity. Steeper inclines increase strain and may necessitate adjustments in running strategy.

    - Distance Covered
        Consider the total distance covered and how it impacts fatigue and performance. Provide feedback on pacing and recovery strategies based on distance.

    Example 1:
    Input:
        Age: 30
        Gender: Male
        JSON Data: "timestamp": "2024-09-04T00:00:00Z", "heartRate": 145, "incline": 5, "distanceCovered": 1.2, "vo2max": 50
    Feedback:
        Maintain your current pace and gradually increase distance.
    Reason:
        1. Your heart rate of 145 bpm is within the moderate zone, suggesting a good level of effort.
        2. With a VO2 Max of 50 ml/kg/min, you have strong endurance, which supports maintaining your current pace.
        3. The 5-degree incline adds moderate intensity; keep monitoring performance as you increase distance.

    Example 2:
    Input:
        Age: 45
        Gender: Female
        JSON Data: "timestamp": "2024-09-04T00:00:00Z", "heartRate": 175, "incline": 8, "distanceCovered": 3.5, "vo2max": 40
    Feedback:
        Consider reducing your pace and focus on recovery with high inclines.
    Reason:
        1. Your heart rate of 175 bpm is high, indicating significant exertion.
        2. With a VO2 Max of 40 ml/kg/min, improving endurance is important.
        3. The 8-degree incline significantly increases intensity, so reducing pace and emphasizing recovery is advisable.

    input: |
    Given the following conditions:
        Person:
        Age: {age}
        Gender: {gender}
        Current Heart Rate: {heart_rate} bpm
        VO2 Max: {vo2max} ml/kg/min
        Current Running Incline: {incline} degrees
        Distance Covered: {distance_covered} km
    Output:
        Feedback: [One-line feedback on future running sessions]
        Reason: [Detailed reasoning behind the feedback]
    """
    return prompt_template
