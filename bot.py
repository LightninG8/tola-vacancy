from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db.client import db

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    # Добавляем пользователя
    db.add_user(message.from_user.id, message.from_user.username)
  
    await message.answer("Привет")


@router.message()
async def on_message(message: types.Message):
  try:
    if message.forward_from != None:
      await bot.forward_message(chat_id=-1002485636124, from_chat_id=message.from_user.id, message_id=message.message_id)
  except Exception as e:
    print(e)
      
