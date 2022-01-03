# Local
import buttons as btn
import strings
from app import BOT_TOKEN, SERVER_HOST, SERVER_REQUEST_GET, SERVER_REQUEST_POST
# Global 
from aiogram import types,Bot, Dispatcher, executor
import json

dp = Dispatcher(Bot(BOT_TOKEN, parse_mode=types.message.ParseMode.HTML))

def touched(user_language):
    with open('titles/strings.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)[user_language]
    return data

@dp.message_handler(commands=['start'])
async def get_start(message: types.Message):
    chat_id = message.chat.id
    pass

@dp.message_handler(commands=['help'])
async def get_help(message: types.Message):
    chat_id = message.chat.id
    pass

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    pass

@dp.callback_query_handler()
async def get_inline_message(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    pass