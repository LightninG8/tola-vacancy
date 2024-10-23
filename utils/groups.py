from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantRequest
from telethon import events
import re
from dotenv import load_dotenv
import os
from db.client import db


load_dotenv()

BOT_USERNAME = os.getenv("BOT_USERNAME")


# Обработка нового поста в канале
categories = db.get_categories()

async def check_post_category(event):
  for category in categories:
    message = event.raw_text.lower()
    keywords = [x.lower() for x in category["keywords"]]
    excluded_keywords = [x.lower() for x in category["excluded_keywords"]]
    
    regex = re.compile('|'.join([r'\b%s\b' % w for w in keywords]), flags=re.I)
    keywords_entries = list(filter((lambda x: x != "" and x != "\n"), regex.findall(message)))
    
    excluded_regex = re.compile('|'.join([r'\b%s\b' % w for w in excluded_keywords]), flags=re.I)
    excluded_keywords_entries = list(filter((lambda x: x != "" and x != "\n"), excluded_regex.findall(message)))
    
    
        
    if (len(excluded_keywords_entries)):
      return None
  
    if (len(keywords_entries)):
      return (category["id"], category["name"])

    return None


# Обработчик новых постов в канале
async def watch_group(client):
    chats_list = [
        -4126756541,
        -1002398870484,
        -1002437501112,
        -1002213805855_5
      ]

    @client.on(events.NewMessage(chats=chats_list))
    async def my_event_handler(event):
      
      try:       
        post_category = await check_post_category(event)
        
    
        if (post_category):
          await client.forward_messages(BOT_USERNAME, event.message)

      except Exception as e:
        print("[watch_group] Some problems...")
      
