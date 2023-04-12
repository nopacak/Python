import requests
import random
import requests
from bs4 import BeautifulSoup


def insult_link_generator():

    #### access the web page ####

    URL = "https://www.foaas.com/operations"

    headers = {'Accept': 'application/json'}
    response = requests.get(URL, headers=headers)


    #### convert response to JSON ####

    response_json = response.json()


    #### hard coded data needed for a link creation ####

    from_name = "Nikolina"
    name = "Nikolina"
    company = "Valcon"
    behavior = "spillin' the tea"
    thing = "teapot"
    reaction = "PANICK"
    tool = "brain"
    language = "common sense"
    do = "wash"
    something = "dishes"



    #### getting all available URL endings ####

    url_list = []

    for i in range(100):
        for key, value in response_json[i].items():
            if key == "url":
                #print(value)
                url_list.append(value)


    #### creating full links ####

    full_url_list = []

    for i in range (100):
        full_url_list.append(f"https://www.foaas.com{url_list[i]}")

    #print(full_url_list)

    #### creating full links with required names ####
    
    full_url_list = [sub.replace(":from", from_name) for sub in full_url_list]
    full_url_list = [sub.replace(":name", name) for sub in full_url_list]
    full_url_list = [sub.replace(":company", company) for sub in full_url_list]
    full_url_list = [sub.replace(":behavior", behavior) for sub in full_url_list]
    full_url_list = [sub.replace(":thing", thing) for sub in full_url_list]
    full_url_list = [sub.replace(":reaction", reaction) for sub in full_url_list]
    full_url_list = [sub.replace(":language", language) for sub in full_url_list]
    full_url_list = [sub.replace(":tool", tool) for sub in full_url_list]
    full_url_list = [sub.replace(":do", do) for sub in full_url_list]
    full_url_list = [sub.replace(":something", something) for sub in full_url_list]

    # print(full_url_list)
    # print()


    #### random number and link creation ####

    random_number = random.randint(0, 99)

    #print(random_number)
    print(full_url_list[random_number])

    return full_url_list[random_number]

#insult_link_generator()



def scrap_the_link():
   
   #### access the web site and parse the data ####
   
   URL_to_scrap = insult_link_generator()
   #print(URL_to_scrap)
   response = requests.get(URL_to_scrap)
   stranica = BeautifulSoup(response.content, "html.parser")

   #### scrap the text ####

   insult_all_data = stranica.find_all('div', class_='hero-unit')
   #print(insult_all_data)

     
   for insult in insult_all_data:
        insult_text = insult.h1.text

   print(insult_text) 
   return insult_text



#scrap_the_link()