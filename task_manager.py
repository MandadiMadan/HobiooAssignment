import json
import os

FILE_NAME = "tasks.json"



def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []



def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)



def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ")

    tasks = load_tasks()

    task = {
        "title": title,
        "priority": priority,
        "done": False
    }

    tasks.append(task)

    save_tasks(tasks)

    print("\nTask added successfully!\n")



def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available.\n")
        return

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    tasks.sort(key=lambda x: priority_order.get(x["priority"], 4))

    print("\n===== TASK LIST =====\n")

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"

        print(f"{index}. {task['title']}")
        print(f"   Priority : {task['priority']}")
        print(f"   Status   : {status}\n")



def mark_done():
    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available.\n")
        return

    list_tasks()

    try:
        task_number = int(input("Enter task number to mark as done: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True

            save_tasks(tasks)

            print("\nTask marked as completed!\n")

        else:
            print("\nInvalid task number.\n")

    except ValueError:
        print("\nPlease enter a valid number.\n")



def delete_task():
    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available.\n")
        return

    list_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)

            save_tasks(tasks)

            print(f"\nTask '{removed_task['title']}' deleted successfully!\n")

        else:
            print("\nInvalid task number.\n")

    except ValueError:
        print("\nPlease enter a valid number.\n")



def main():

    while True:

        print("===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            mark_done()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("\nExiting Task Manager...")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()