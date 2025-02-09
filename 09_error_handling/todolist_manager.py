import json

file_name = 'Todo_list.json'

def load_list():
    try:
        with open(file_name ,'r') as file:
           list_data = json.load(file)
        return list_data
    except FileNotFoundError:
        return []


def save_method(tasks):
    with open(file_name ,'w') as file:
            json.dump(tasks ,file)

def list_all_task(tasks):
    print("\n")
    print("*" * 70)
    for idx , task in enumerate(tasks ,start=1):
        print(f"{idx}. Name: {task['name'] } - Day: {task['day']} ")
    print("*" * 70)


def add_task(tasks):
    name = input("Enter The Task Name: ")
    day =  input("Enter The Day: ")
    tasks.append({'name':name , 'day':day})
    save_method(tasks)

def update_task(tasks):
    list_all_task(tasks)
    index = int(input("Enter the Number of task you want to Update: ").strip())
    
    if 1 <= index <= len(tasks):
        single_task = tasks[index -1]
        n_name = input("Change the name: ") or single_task['name']
        n_day  = input("Change the Day: ")  or single_task['day']
        tasks[index-1] = {"name":n_name , "day":n_day}
        save_method(tasks)
    else:
        print("Invalid Number")


def delete_task(tasks):
    list_all_task(tasks)
    index = int(input("Enter the Number of task you want to Update: ").strip())
    
    if 1 <= index <= len(tasks):
        del tasks[index-1]
        save_method(tasks)
    else:
        print("Invalid Number")




def main():
    tasks=load_list()
    while True:
        print("What do you want to do?")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update Task")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Enter The number: ")

        match choice:
            case '1':
                list_all_task(tasks)
            
            case '2':
                add_task(tasks)

            case '3':
                update_task(tasks)

            case '4':
                delete_task(tasks)

            case '5':
                break

if __name__ == "__main__":
    main()


    