#!/usr/bin/python3
"""review how to make an API request with Python"""

# standard library import
import urllib.request
import json # part of the standard library -- required to change plain text into JSON

# define our URI
#uri = 'https://pokeapi.co/api/v2/pokemon/pikachu'
uri = 'http://api.open-notify.org/astros.json'

# make a lookup to our URI
response = urllib.request.urlopen(uri)
# GET /api/v2/pokemon/pikachu   ------------------------------------->    https://pokeapi.co:443
#                               <------------------------------------     200 'OK' + json

## ensure we received a 200 response
if response.code != 200:
    print("Uh oh! A non 200 status code was recieved. Returned was", response.status_code)
    exit()

## we know we have a 200 response that *should* have JSON on it
## strip the JSON off and convert to python lists & dicts
response_read_as_str = response.read().decode("utf-8")
print(response_read_as_str)
print(type(response_read_as_str))

#print(response_read_as_str[10:35])
response_converted_to_dict = json.loads(response_read_as_str)

print(response_converted_to_dict)
print(type(response_converted_to_dict))
print(response_converted_to_dict.get("people")) # this WORKS! the data is no longer string data
print(response_converted_to_dict.get("people")[4])

#
## pick out keys that you want to see response_json.get('you_key')
#print(response_json)
#
#print(response_json.get("name"))
#print(response_json.get("id"))
#print(response_json.get("abilities"))
