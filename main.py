# Local Modules
from app import config
import buttons as btn
import strings
from genius import chunk, request, touched

# Database
from db.models import User, Admin
from db.dispatcher import *

# Aiogram Modules
from aiogram import types,Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext 
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Filter


storage = RedisStorage2(config()["telegram"]["token"], 6379, db=5, pool_size=10, prefix='my_fsm_key') if config()["system"]["redis"]["status"] else MemoryStorage()

local_session = Session(bind=engine)


bot = Bot(config()["telegram"]["token"], parse_mode=types.message.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


# All states
class IsAdmin(Filter): 
    key = "is_admin"

    async def check(self, message: types.Message):
        admins = objects_all(session=local_session, model=Admin)
        list_admin = list(map(lambda i: int(i.telegram_id), admins))
        return message.chat.id in list_admin


class States(StatesGroup):
    request_phone = State()
    request_language = State()


# state= States.request_phone or '*' <- all
@dp.message_handler(commands=['start'], state='*')
async def get_start(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    user = get_or_create(session=local_session, model=User, telegram_id=chat_id)
    local_session.commit()


@dp.message_handler(commands=['help'], state='*')
async def get_help(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    text = "This bot created with <b>pribot v1</b>"
    await bot.send_message(chat_id=chat_id, text=text)
    
    

@dp.callback_query_handler(text=["uz", "ru", "en"], state=States.request_language)
async def get_language(callback: types.CallbackQuery, state: FSMContext):
    chat_id = callback.message.chat.id

    await state.finish()
    await States.request_phone.set()
    # or 
    # await States.next()

# Filter Number 
@dp.message_handler(content_types=["contact"], state=States.request_phone)
async def get_phone_number(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    #! Recomended 
    # phone_number = message.contact.phone_number.replace('+', '')

    await state.finish()


executor.start_polling(dp)