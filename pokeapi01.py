#!/usr/bin/python3
"""review how to make an API request with Python"""

# import remote
# remote object
# print(remote.batteries)   # no parens on 'batteries', just means we want this value
# 2

# remote.channel('up')  # () means execute
# action is do change the channel using the remote object

# from remote import batteries
# batteries.voltage()


# non-standard library to make an API request
import requests

# define our URI
uri = 'https://pokeapi.co/api/v2/pokemon/'

# make a lookup to our URI
response = requests.get(uri + 'pikachu')
# GET /api/v2/pokemon/pikachu   ------------------------------------->    https://pokeapi.co:443
#                               <------------------------------------     200 'OK' + json

# ensure we received a 200 response
if response.status_code != 200:
    print("Uh oh! A non 200 status code was recieved. Returned was", response.status_code)
    exit()

# we know we have a 200 response that *should* have JSON on it
# strip the JSON off and convert to python lists & dicts
response_json = response.json()

# pick out keys that you want to see response_json.get('you_key')
print(response_json)

print(response_json.get("name"))
print(response_json.get("id"))
print(response_json.get("abilities"))
