from math import ceil 
from app import config
import requests
import json


def chunk(arr, size):
    return list(map(lambda x: arr[x * size:x*size+size], list(range(0, ceil(len(arr)/ size)))))


def touched():
    with open('titles/buttons.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def request(link, params: dict = None, json: dict = None) -> dict:
    if params: 
        request = requests.post(config()["django"]["host"] + link, params=params).json()
    elif json: 
        request = requests.post(config()["django"]["host"] + link, json=json).json()
    return request
