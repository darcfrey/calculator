# def calculate_cgpa(subjects):
#     total_credit_unit = 0
#     total_grade = 0
    
#     for subject in subjects:
#         grade = input("Enter grade obtained in {}: ".format(subject))
#         unit = int(input("Enter credit unit for {}: ".format(subject)))
        
#         # Calculate grade points
#         if grade == 'A':
#             grade_point = 4
#         elif grade == 'B':
#             grade_point = 3
#         elif grade == 'C':
#             grade_point = 2
#         elif grade == 'D':
#             grade_point = 1
#         else:
#             grade_point = 0  # assuming 'F' or other non-graded values
            
#         # Calculate total grade points
#         total_grade += grade_point * unit
#         total_credit_unit += unit
    
#     # Calculate CGPA
#     cgpa = total_grade / total_credit_unit
    
#     return cgpa

# def main():
#     num_subjects = int(input("Enter the number of subjects: "))
#     subjects = []
#     for i in range(num_subjects):
#         subject_name = input("Enter name of subject {}: ".format(i+1))
#         subjects.append(subject_name)
    
#     cgpa = calculate_cgpa(subjects)
#     print( float(cgpa))





import math
from datetime import datetime

def calculate_solar_position(latitude, longitude, date_time):
    """
    Calculates the solar position (altitude and azimuth) for a given location and time.

    Args:
    latitude (float): Latitude of the location in degrees (-90 to 90).
    longitude (float): Longitude of the location in degrees (-180 to 180).
    date_time (datetime): Date and time for which to calculate the solar position.

    Returns:
    tuple: Tuple containing the solar altitude and azimuth angles in degrees.
    """
    # Convert latitude and longitude to radians
    lat_rad = math.radians(latitude)
    lon_rad = math.radians(longitude)

    # Calculate the number of days since the start of the year
    day_of_year = date_time.timetuple().tm_yday

    # Calculate the solar declination angle (in radians)
    declination = 23.45 * math.sin(math.radians(360/365 * (day_of_year - 81)))

    # Calculate the equation of time
    B = (360/364) * (day_of_year - 81)
    EoT = 9.87 * math.sin(2 * math.radians(B)) - 7.53 * math.cos(math.radians(B)) - 1.5 * math.sin(math.radians(B))

    # Calculate the solar hour angle (in degrees)
    solar_time = date_time.hour + (date_time.minute / 60) + (date_time.second / 3600) - (longitude / 15) + EoT / 60
    hour_angle = (solar_time - 12) * 15

    # Calculate the solar altitude angle (in degrees)
    altitude = math.degrees(math.asin(math.sin(lat_rad) * math.sin(math.radians(declination)) +
                                      math.cos(lat_rad) * math.cos(math.radians(declination)) *
                                      math.cos(math.radians(hour_angle))))

    # Calculate the solar azimuth angle (in degrees)
    azimuth = math.degrees(math.atan2(-math.sin(math.radians(hour_angle)),
                                      -math.cos(math.radians(hour_angle)) * math.sin(lat_rad) +
                                      math.tan(math.radians(declination)) * math.cos(lat_rad)))

    # Adjust azimuth angle to be between 0 and 360 degrees
    azimuth = (azimuth + 360) % 360

    return altitude, azimuth

def is_shaded(building_orientation, latitude, longitude, times_to_shade):
    """
    Determines if the building is shaded at specific times.

    Args:
    building_orientation (float): Orientation of the building in degrees (0-360), where 0 is north.
    latitude (float): Latitude of the building location in degrees (-90 to 90).
    longitude (float): Longitude of the building location in degrees (-180 to 180).
    times_to_shade (list of datetime objects): List of specific times to check for shading.

    Returns:
    list of bool: List indicating whether the building is shaded at each specific time.
    """
    is_shaded_list = []
    for time_to_shade in times_to_shade:
        solar_altitude, solar_azimuth = calculate_solar_position(latitude, longitude, time_to_shade)
        sun_azimuth_relative = solar_azimuth - building_orientation
        if abs(sun_azimuth_relative) > 90:
            is_shaded_list.append(True)
        else:
            is_shaded_list.append(False)
    return is_shaded_list

# Example usage
building_orientation = 180  # Building faces south
latitude = 80  # Latitude of New York City
longitude = -23  # Longitude of New York City
times_to_shade = [datetime(2024, 2, 25, 9, 0, 0), datetime(2024, 2, 25, 12, 0, 0), datetime(2024, 2, 25, 15, 0, 0)]

shading_status = is_shaded(building_orientation, latitude, longitude, times_to_shade)
print(shading_status)

"""import pandas as pd
import openai
from transformers import pipeline
open_ai_api= (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)
data = pd.read_excel("chatbot_data.xlsx")   

responses = {}
for idx, row in data.iterrows():
    user_input = row['user_input'].lower()
    bot_response = row['bot_responses']
    responses[user_input] = bot_response


chatbot = pipeline("text-generation", model="gpt2")  # Initialize the chat bot using the pipeline


print("Darcbot: Hi! I'm your chatbot")  # Interraction loop
while True:
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        print("Darcbot: Goodbye!")
    
    if user_input in responses:
         print("Darcbot:", responses[user_input])
    else:
        bot_response =  chatbot(user_input)[0]['generate_text']
        print("Darcbot:", bot_response.strip())
        # Add the user input and bot response to the responses dictionary
        responses[user_input] = bot_response.strip()
        # Save the responses to the excel file
    data.to_excel("book.xlsx", index=False)
        # Save the responses to the excel file"""



        """import pandas as pd
from transformers import pipeline
data=pd.read_csv("book.csv")#the dictionary
print(data)
response={}
for ide, row in data.iterrows():
    user_input=row('INPUT QUESTIONS')
    bot_response=row('BOT RESPONSES')
    response(user_input)== bot_response

while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("AI: Goodbye!")
            break

        bot_response = response(user_input)
        print("AI:", bot_response)"""

