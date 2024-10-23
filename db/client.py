import os
import certifi
import json

from pymongo import MongoClient
from bson.json_util import dumps
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("MONGO_STRING")

class MongoDB(object):
  def __init__(self, string: str, db_name: str):
    self._client = (MongoClient(string, tlsCAFile=certifi.where()))[db_name]
    self.users = self._client["users"]
    
  def add_user(self, id, username):  
    try:
      count = self.users.count_documents({"user_id": id})
    
      # Добавляем пользователя
      if count == 0:
        return json.loads(dumps(self.users.insert_one({
          "user_id": id,
          "username": username,
          "categories": []
        })))
    except Exception as e:
      print("[add_user] Some problem...")
      print(e)
  def get_users(self):  
    try:
      return json.loads(dumps(self._client["users"].find()))
    except Exception as e:
      print("[get_users] Some problem...")
      print(e)

  def get_accounts(self):
    try:
      return json.loads(dumps(self._client["accounts"].find()))
    except Exception as e:
      print("[get_accounts] Some problem...")
      print(e)
  
  def get_proxies(self):
    try:       
      return json.loads(dumps(self._client["proxies"].find()))
    except Exception as e:
      print("[get_proxies] Some problem...")
      print(e)
  
  def get_groups(self):
    try:       
      return json.loads(dumps(self._client["channels"].find()))
    except Exception as e:
      print("[get_groups] Some problem...")
      print(e)
  
  def get_categories(self):
    try:       
      return json.loads(dumps(self._client["categories"].find()))
    except Exception as e:
      print("[get_categories] Some problem...")
      print(e)
  

db = MongoDB(CONNECTION_STRING, 'TolaVacancy')
