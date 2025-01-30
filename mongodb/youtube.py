from bson import ObjectId
from pymongo import MongoClient 

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.msysl.mongodb.net/")

db = client["ytmanager"]
video_collection =db["videos"]

print(video_collection)

def list_video():
    for video in video_collection.find():
        print(f"ID:{video['_id']}, Name:{video['name']} and time:{video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name": name,"time":time})

def update_video(video_id,name,time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {"$set":{"name": name,"time": time}}
         )
                          

def delete_video(video_id):
    video_collection.delete_one({'_id':ObjectId(video_id)})

def main():
    while True:
        print("\n youtube manager app")
        print("1. list all video")
        print("2. add a new video")
        print("3. update a video ")
        print("4. delete a video")
        print("5. exit the application")
        choice = input("Enter your choice ")
        
        if choice =='1':
            list_video()
        elif choice == '2':
            name = input("enter the video name:")
            time = input("enter the video time :")
            add_video(name,time)
        elif choice == '3':
            video_id = input("enter the video id to :")
            name = input("enter the update video")
            time = input("enter the update time")
            update_video(video_id,name,time)
        elif choice == 4:
            video_id = input("enter the video id to :")
            delete_video(video_id,name,time)
        elif choice == 5:
            break
        else:
            print("invalid choice")
        

if __name__ == '__main__':
    main()
