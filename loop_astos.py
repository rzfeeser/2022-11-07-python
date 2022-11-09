#!/usr/bin/python3
"""Learning looping with astro data"""

# make an HTTP lookup to an API


# check the response (did we get back a 200 response?)


# peel JSON off of the response


# decode the JSON into Python data (for now, we'll just hardcode the data into our program)
astro_data = {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}


# parse python data and display Names and Crafts of Astros
#astro_data_people = astro_data.get("people")
#
#for people in astro_data_people:
#    #print(people)
#    #print(people.get("name"))
#    print(people.get("name"), "is riding on the", people.get("craft"))

for people in astro_data.get("people"):
    print(people.get("name"), "is riding on the", people.get("craft"))
