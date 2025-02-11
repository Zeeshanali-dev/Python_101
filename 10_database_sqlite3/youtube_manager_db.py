import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    time TEXT NOT NULL
)
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    print("\n")
    print("*" * 70)
    for row in videos:
        print(row)
        # print(f"{row[0]}. Name: {row[1]} - Time: {row[2]}")
    print("*" * 70)

def add_video( name, time):
    cursor.execute("INSERT INTO videos (title, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video( _id, name, time):
    cursor.execute("UPDATE videos SET title = ?, time = ? WHERE id = ?", (name, time, _id))
    cursor.commit()

def delete_video(_id): 
    cursor.execute("DELETE FROM videos WHERE id = ?", (_id,))
    conn.commit()  



def main():
    while True:
        print("\n Youtube Manager DB | choose an option")
        print("1. List all Youtube  videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ").strip()


        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)

        elif choice == "3":
            _id = int(input("Enter the index of the video you want to update: "))
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(_id,name, time)

        elif choice == "4":
            _id = int(input("Enter the index of the video you want to update: "))
            delete_video(_id)

        elif choice == "5":
            break

        else:
            print("Invalid Choice")
        
    conn.close()

        # match choice:
        #     case "1":
        #         list_videos()

        #     case "2":
        #         add_video()

        #     case "3":
        #         update_video()

        #     case "4":
        #         delete_video()

        #     case "5":
        #         break

        #     case _:
        #         print("Invalid Choice")


if __name__ == "__main__":
    main()