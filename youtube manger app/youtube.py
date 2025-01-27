import json 

def load_data():
    try:
        with open('yorutube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        pass
        return []

def save_data_helper(video):
    with open('youtube.txt','w') as file:
        json.dump(video,file)


def list_all_videos(video):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(video, start=1):    
        print(f"{index}.{video["name"]},duration :{video["time"]}")
        print("\n")
        print("*" * 70)
        
def add_video(video):
    name = input("enter video name :")
    time = input("enter the time :")
    video.append({'name':name,'time':time})
    save_data_helper(video)
    
def update_video(video):
    list_all_videos(video)
    index = int(input("enter the number to update"))
    if 1<= index <=len(video):
        name = input("enter the new video name")
        time = input("enter the new time")
        video[index-1] ={'name' :name,'time': time}
        save_data_helper(video)
    else:
        print("invalid index selected")

def delete_video(video):
    list_all_videos(video)
    index = int(input("enter the video number to be deleted"))
    if 1<= index <= len(video):
        del video[index-1]
        save_data_helper(video)
    else:
        print("invalid video index selected")
def main():
    video = load_data()
    while True:
        print("\n youtube manger | option an app")
        print("1 list all youtube video")
        print("2 like all the video")
        print("3 comment all the video")
        print("4 subsrube my channel")
        print("5 notofication my channel")
        choice = input("enter your choice")

        match choice :
            case "1":
             list_all_videos(video)   
            case "2":
             add_video(video)
            case "3":
             update_video(video)
            case "4":
             delete_video(video)
            case "5":
             break
            case "6":
             print("invalid choice")
        
if __name__ ==  "__main__":
    main() 
