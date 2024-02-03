from pymongo import MongoClient
import os
from datetime import datetime
import pytz

# Connect to MongoDB
mongo_client = MongoClient(os.getenv('mongodb'))
db = mongo_client['Sites']
collection = db['redirect']

def log(request, url):
    collection.insert_one({
        "url_set": url,
        "by_ip": request.headers.get('X-Forwarded-For', request.remote_addr),
        "user": request.headers.get('User-Agent', 'N/A'), 
        "time": datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")
    })

def access(request, url):
    collection.insert_one({
        "redirect_url": url,
        "ip": request.headers.get('X-Forwarded-For', request.remote_addr),
        "redirected_user": request.headers.get('User-Agent', 'N/A'), 
        "time": datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")
    })
