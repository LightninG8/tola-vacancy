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
      -1001804485641,
      -1001545309331,
      -1002213805855,
      -1002398870484,
      -1002437501112,
      -1002232235769,
      -1002150190638,
      -1002436107687,
      -1002049255497,
      -1002113569223,
      -1002195635669,
      -1002338225466,
      -101480501,
      -1002444623569,
      -1002454648609,
      -4513615535,
      -1001881557942,
      -1001549994889,
      -1001955228980,
      -1001180938632,
      -1001776032979,
      -1001949086996,
      -1002175928963,
      -1001561949320,
      -1001678631393,
      -1001972638622,
      -1001949037720,
      -1002183547028,
      -1001824331499,
      -1001100339332,
      -1001949949527,
      -1001480867611,
      -1001852257203,
      -1001416412699,
      -1001548363362,
      -1001551866547,
      -1001454051820,
      -1001656920813,
      -1001777153335,
      -1001642763128,
      -1001830403663,
      -1001352099000,
      -1001688180025,
      -1001572459593,
      -1001887065342,
      -1002237169459,
      -1001154995805,
      -1001849399495,
      -1001242285573,
      -4126756541,
      -1002398870484,
      -1002437501112,
      -1002213805855
    ]


    @client.on(events.NewMessage(chats=chats_list))
    async def my_event_handler(event):
      try:       
        post_category = await check_post_category(event)
            
        if (post_category):
          print(post_category)
          await client.forward_messages(BOT_USERNAME, event.message)

      except Exception as e:
        print("[watch_group] Some problems...")
      
