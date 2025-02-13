from pymongo import MongoClient
from bson import ObjectId

##client is in  env /fil//e

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    print("\n")
    print("*" * 70)
    for video in video_collection.find():
        print(f"ID: {video['_id']} , Name: {video.get('name', 'Unknown')} - Time: {video.get('time', 'Unknown')}")
    print("*" * 70)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})
    

def update_video(video_id, n_name, n_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {'$set': {"name": n_name, "time": n_time}})


def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                list_all_videos()

            case "2":
                name = input("Enter video name: ").strip()
                time = input("Enter video time: ").strip()
                add_video(name, time)
                print("✅ Video added successfully!")

            case "3":
                video_id = input("Enter Video ID: ").strip()
                new_name = input("Enter new video name: ").strip()
                new_time = input("Enter new video time: ").strip()
                try:
                    update_video(video_id, new_name, new_time)
                    print("✅ Video updated successfully!")
                except Exception as e:
                    print(f"❌ Error: {e}")

            case "4":
                video_id = input("Enter Video ID: ").strip()
                try:
                    delete_video(video_id)
                    print("✅ Video deleted successfully!")
                except Exception as e:
                    print(f"❌ Error: {e}")

            case "5":
                print("Exiting... Goodbye!")
                break

            case _:
                print("❌ Invalid Choice! Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()





