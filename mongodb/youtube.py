from pymongo import MongoClient 

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.msysl.mongodb.net/")

db = client["ytmanager"]
video_collection =db["videos"]

print(video_collection)