def show_menu():
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

def view_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\nNo tasks found.")
    except FileNotFoundError:
        print("\nNo tasks found.")

def add_task():
    task = input("Enter a new task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{removed.strip()}' deleted.")
        else:
            print("Invalid task number.")
    except (ValueError, FileNotFoundError):
        print("Error deleting task.")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
