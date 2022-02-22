import requests
from flask import abort


AUTH_USER = 'marcelo@leafworks.de/token' 
AUTH_PASSWORD = 's4jQu3XinhR2aTtRSt09mo06SmqC9eIMcDCaF9b2'

def get_call(url):
    response = requests.get(
        url, 
        auth=(AUTH_USER, AUTH_PASSWORD)
    )
    if (response.status_code == 200):
        return response.json()
    else:
        abort(response.status_code)

def post_call(url, data):
    response = requests.post(
        url, 
        json=data,
        auth=(AUTH_USER, AUTH_PASSWORD)
    )
    if (response.status_code == 200):
        return response.json()
    else:
        abort(response.status_code)

def put_call(url, data):
    response = requests.put(
        url, 
        json=data,
        auth=(AUTH_USER, AUTH_PASSWORD)
    )
    if (response.status_code == 200):
        return response.json()
    else:
        abort(response.status_code)