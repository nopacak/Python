from random import randrange
from sensors import *
#print(randrange(10))

data = get_temperature_brightness_soil()

temperature = f"Temperature is: {data[0]}\u00b0C"
brightness = f"Brightness is: {data[1]} %"
soil_temperature = f"Soil temperature is: {data[2]}\u00b0C"
soil_moisture = f"Soil moisture is: {data[3]} m\u00b3/m\u00b3"

print(temperature, brightness, soil_temperature, soil_moisture, sep="\n")
