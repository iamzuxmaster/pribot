from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json

def strings(user_language):
    with open('titles/buttons.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

    return data[user_language]

def select_language():
    langs = [
        {
            "title": "🇺🇿 O'zbek",
            "code": "uz"
        },
        {
            "title": "🇷🇺 Русские",
            "code": "ru"
        },
        {
            "title": "🇺🇸 English",
            "code": "en"
        }
    ]
    keys = [
        [InlineKeyboardButton(text=i["title"], callback_data=i["code"])]
        for i in langs
    ]

    return InlineKeyboardMarkup(inline_keyboard=keys)