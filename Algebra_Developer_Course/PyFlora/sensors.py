#This file is retrieving the simulated sensor data from https://open-meteo.com/

import requests
import json
from random import randrange

# Define lat and lon of your location (Zagreb in this case)
lat = "45.81"
lon = "15.98"

def get_temperature_brightness_soil():

    global lat
    global lon
    
    # Build URL
    URL = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,cloudcover,soil_temperature_6cm,soil_moisture_3_9cm"
    headers = {'Accept': 'application/json'}
    
    
    # Make a GET request to the API
    response = requests.get(URL, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:

        # Retrieve the JSON data from the response
        data = json.loads(response.text)

        # Print the weather data
        #print(data)

        # Dump the data into a json file
        try:
            with open("open_meteo.json", "w", encoding="utf-8") as file_stream:
                json.dump(data, file_stream)
        except Exception as e:
            print(f"Error - {e}")
    else:
        # If the request was not successful, print the status code and reason
        print(f"Request failed with status code {response.status_code} - {response.reason}")


    i = randrange(167)  # there are 168 results for the whole day and we are randomly shuffling through them to simulate sensor condition detection 

    temperature = data["hourly"]["temperature_2m"][i]
    brightness = data["hourly"]["cloudcover"][i]
    soil_temperature = data["hourly"]["soil_temperature_6cm"][i]
    soil_moisture = data["hourly"]["soil_moisture_3_9cm"][i]

    #print(f"Temperature is: {temperature}\u00b0C \nBrightness is: {brightness}% \nSoil Temperature is : {soil_temperature}\u00b0C \nSoil Moisture is: {soil_moisture}m\u00b3/m\u00b3")

    return temperature, brightness, soil_moisture, soil_temperature


#get_temperature_brightness_soil()