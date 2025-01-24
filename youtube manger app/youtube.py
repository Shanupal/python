import json 

def load_data():
    try:
        with open('yorutube.txt','r')
    except:
        pass

def list_all_videos():
    pass
def update_video(video):
    pass
def update_video(video):
    pass
def delete_video(video):
    pass

while True:
    print("\n youtube manger | option an app")
    print("1 list all youtube video")
    print("2 like all the video")
    print("3 comment all the video")
    print("4 subsrube my channel")
    print("5 notofication my channel")
    
    choice = input("enter the number")
    match choice :
        case "1":
            list_all_videos(video)   
        case "2":
            all_video(video)
        case "3":
            update_video(video)
        case "4":
            delete_video(video)
        case "5":
            break
        case "6":
        print("invalid choice")
        
