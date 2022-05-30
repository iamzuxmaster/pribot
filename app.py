import json 

def config(file_path:str="./config.json") -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data

def languages(file_path:str="./titles/buttons.json") -> dict: 
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data["languages"]