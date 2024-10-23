from utils.groups import watch_group
from db.client import db

from telethon import TelegramClient
from telethon.sessions import StringSession

async def account_work(client):
  await client.start()

  try:
    my_id = (await client.get_me()).id
    
    print(f'[{my_id}] - Start')
    
      
    # Прослушивание всех чатов
    await watch_group(client)
          

  except Exception as e:
    print("[work] Some problem...")
    print(e)
    
  await client.run_until_disconnected()
  
      
  

