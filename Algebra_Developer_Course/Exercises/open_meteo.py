import requests
import json

def get_sunrise_and_sunset_time():

    # Define lat and lon of your location (Zagreb in this case!)
    lat = "45.81"
    lon = "15.98"
    
    # Build URL
    URL = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,rain,showers,snowfall&daily=sunrise,sunset&forecast_days=1&timezone=auto"
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
            print(f"Dogodila se greska - {e}")
    else:
        # If the request was not successful, print the status code and reason
        print(f"Request failed with status code {response.status_code} - {response.reason}")

    # Parse the data to get sunrise and sunset time
    sunrise = data["daily"]["sunrise"][0]
    sunset = data["daily"]["sunset"][0]
    print("Sunrise:", sunrise)
    print("Sunset:", sunset)


get_sunrise_and_sunset_time()