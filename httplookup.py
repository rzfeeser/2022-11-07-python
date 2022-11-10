#!/usr/bin/python3

# python3 -m pip install requests
import requests  # see requests webpage for usage


result = requests.get('http://api.open-notify.org/astros.json')

print(dir(result))

# if we want to see the JSON attached to the result
print(result.json())

print()

result_json = result.json()
print(result_json)


for astro in result_json.get("people"):
    print(astro.get("name"), "is riding on the", astro.get("craft"))
