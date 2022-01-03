import requests
from json import load

def strings(user_language):
    with open('titles/strings.json', 'r', encoding='UTF-8') as file:
        data = load(file)
    return data[user_language]

def select_language():
    # Please note Unused language
    text = "🇺🇿 Iltimos tilni tanlang..."
    text += "🇷🇺 Пожалуйста выберите язык"
    text += "🇺🇸 Please select a language"
    # ? Ex: text += "🇹🇷 Lütfen bir dil seçin" 
    return text