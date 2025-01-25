import sqlite3
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.create_window_function()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
                   
                   )
                   ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?.?)",(name,time))
    conn.commit()

def update_video(video_id, new_name,new_time):
    cursor.execute("UPDATE videos SET name=?, time=?, WHERE id =?",(new_name,new_time,video_id))

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id= ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\n youtube manger app with bd")
        print("1. list video ")
        print("2. add video")
        print("3. update video")
        print("4. delete vide")
        print("5. exit app")
        choice = input("enter your choicse: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("enter the video name: ")
            time = input("enter the video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("enter video id to update: ")
            name = input("enter the video name: ")
            time = input("enter the video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("enter video id to delete")
            
            delete_video(video_id)
            
        elif choice =='5':
            break
        else:
            print("invalid choice")

    conn.close()
if __name__=="__main__":
    main()
