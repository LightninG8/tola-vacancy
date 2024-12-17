import asyncio
from dotenv import load_dotenv
import os
import asyncio
import logging


from telethon import TelegramClient
from telethon.sessions import StringSession
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


from db.client import db
from utils.proxies import format_proxy
from account import account_work
from bot import router, bot, dp

# Запускаем аккаунты
async def bootstrap_accounts():
  accounts = db.get_accounts()
  proxy = format_proxy(db.get_proxies()[0])
  
  clients_list = []
  
  # TODO: Запускаем один акк
  accounts = [accounts[0]]
  
  for account in accounts:
    clients_list.append(account_work(TelegramClient(StringSession(account["string_session"]), account["app_id"], account["app_hash"])));
  
  await asyncio.gather(*clients_list)


# Запускаем бота

async def bootstrap_bot():
  dp.include_routers(router)

  await dp.start_polling(bot)
  
  
# Запускаем приложение
async def main():
  await asyncio.gather(*[bootstrap_accounts(), bootstrap_bot()])
  
if __name__ == '__main__':
    asyncio.run(main())
