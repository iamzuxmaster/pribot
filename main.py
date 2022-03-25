# Global
import json
import jmespath
import requests 

# local
from app import *
import buttons as btn
import strings

# Aiogram
from aiogram import types,Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext 
from aiogram.dispatcher.filters.state import State, StatesGroup

storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='my_fsm_key') if REDIS_STORAGE else MemoryStorage()


bot = Bot(BOT_TOKEN, parse_mode=types.message.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

def touched():
    with open('titles/buttons.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def request(link, params: dict = None, json: dict = None) -> dict:
    if params: 
        request = requests.post(SERVER_HOST + link, params=params).json()
    elif json: 
        request = requests.post(SERVER_HOST + link, json=json).json()
    return request


@dp.message_handler(commands=['start'])
async def get_start(message: types.Message):
    chat_id = message.chat.id

@dp.message_handler(commands=['help'])
async def get_help(message: types.Message):
    chat_id = message.chat.id

@dp.callback_query_handler(text=["uz", "ru", "en"])
async def get_language(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id

@dp.message_handler(content_types=["contact"])
async def get_phone_number(message: types.Message):
    chat_id = message.chat.id


executor.start_polling(dp)