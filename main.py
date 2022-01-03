# Local
import buttons as btn
import strings
from app import BOT_TOKEN, SERVER_HOST, GET, POST
import genius
# Global 
from aiogram import types,Bot, Dispatcher, executor
import json

bot = Bot(BOT_TOKEN, parse_mode=types.message.ParseMode.HTML)
dp = Dispatcher(bot)

user = {}
session = {}
def touched(user_language):
    with open('titles/strings.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)[user_language]
    return data

def sttrs(user_languge):
    main_menu = ''
    return {'main_menu': main_menu}

def keys(user_language):
    main_menu = ''
    return {'main_menu': main_menu}

# Start
@dp.message_handler(commands=['start'])
async def get_start(message: types.Message):
    chat_id = message.chat.id
    pass

# Help - information.
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

executor.start_polling(dp)