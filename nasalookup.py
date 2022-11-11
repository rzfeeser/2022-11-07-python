#!/usr/bin/python3

import requests

def cred_grab():
    # pull in api key
    with open("/home/student/nasa.key") as nkf:
        demokey = nkf.read()
    return demokey.strip()   # ensures what we read out is free of excessive _ and \n characters

def main():

    r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={cred_grab()}")
    #r.json()
    myjson = r.json()
    print(myjson.get("hdurl"))

if __name__ == "__main__":
    main()
