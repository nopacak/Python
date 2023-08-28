from random import randrange
from sensors import *
#print(randrange(10))
from db_manager.userbase import check_login

# condition_data = get_temperature_brightness_soil()

# # temperature = f"Temperature is: {condition_data[0]}\u00b0C"
# # brightness = f"Brightness is: {condition_data[1]} %"
# # soil_temperature = f"Soil temperature is: {condition_data[2]}\u00b0C"
# # soil_moisture = f"Soil moisture is: {condition_data[3]} m\u00b3/m\u00b3"

# # print(temperature, brightness, soil_temperature, soil_moisture, sep="\n")

# plant_data = {1:["Daffodil", "assets\\plant_images\\Daffodil.jpeg", "23.1", "tamno", "hladnije", False],
#               2:["Daisy", "assets\\plant_images\\Daisy.jpeg", "16.5 m3/m3", "tamno", "hladnije", False],
#               3:["Gladiolus", "assets\\plant_images\\Gladiolus.jpeg", "13 m3/m3", "tamno", "hladnije", False],
#               4:["Lilly", "assets\\plant_images\\Lilly.jpeg", "9.08 m3/m3", "tamno", "hladnije", False],
#               5:["Magnolia", "assets\\plant_images\\Magnolia.jpeg", "31 m3/m3", "tamno", "hladnije", False],
#               6:["Orchid", "assets\\plant_images\\Orchid.jpeg", "daily", "tamno", "hladnije", False],
#               7:["Peony", "assets\\plant_images\\Peony.jpeg", "daily", "tamno", "hladnije", False],
#               8:["Poppy", "assets\\plant_images\\Poppy.jpeg", "daily", "tamno", "hladnije", False],
#               9:["Sunflower", "assets\\plant_images\\Sunflower.jpeg", "daily", "tamno", "hladnije", False],
#               10:["Violet", "assets\\plant_images\\Violet.jpeg", "daily", "tamno", "hladnije", False]}

# #condition_data = get_temperature_brightness_soil()
# print (str(condition_data[1]))
# print (plant_data[1][2])
# print(float(condition_data[3]) == float(plant_data[1][2]))

print(check_login("admin", "notadmin"))







