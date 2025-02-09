import json

file_name = 'youtube.json'
def load_data():
    try:
        with open(file_name, 'r') as file:
            test = json.load(file)
            # print(test)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with  open(file_name, "w") as file:
        json.dump(videos , file)  

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for idx, video in enumerate(videos , start=1):
        print(f"{idx}. {video['name']} - Duration: {video['time']}")
    print("*" * 70)

def add_video(videos):
    name= input("Enter video name: ")
    time = input("Enter Video time: ")
    videos.append({"name":name , 'time':time})
    save_data_helper(videos)

def update_video(vedios):
    list_all_videos(vedios)
    index = int(input("Enter the index of the video you want to update: "))

    if 1<= index <= len(vedios):
        name= input("Enter video name: ")
        time = input("Enter Video time: ")
        vedios[index-1] = {"name":name , 'time':time}
        save_data_helper(vedios)
    else:
        print("Invalid index")


def delete_video(vedios):
    list_all_videos(vedios)
    index = int(input("Enter the number of the video you want to delete: "))

    if 1<= index <= len(vedios):
        del vedios[index-1]
        save_data_helper(vedios)
    else:
        print("Invalid index")

def main():
    videos = load_data()
    while  True:
        print("\n Youtube Manager | choose an option")
        print("1. List all Youtube  videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice= input("Enter your choice: ").strip()
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)

            case "2":
                add_video(videos)

            case "3":
                update_video(videos)

            case "4":
                delete_video(videos)

            case "5":
                break 

            case _:
                print("Invalid Choice") 

if __name__ == "__main__":
    main()     
