# 📝 To-Do List App

def show_menu():
    print("\n=== To-do List Menu ===")
    print("1. View To-do List")
    print("2. Add To-do Item")
    print("3. Remove To-do Item")
    print("4. Exit")


def view_todo_list():
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
            if len(tasks) == 0:
                print("\nNo tasks yet. ✅")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("\nNo tasks file found. Your to-do list is empty.")


def add_todo_item():
    task = input("Enter the task to add: ")
    with open("todo_list.txt", "a") as file:
        file.write(task + "\n")
    print(f'✅ Task "{task}" added to the list.')


def remove_todo_item():
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("⚠️ No tasks to remove.")
            return

        view_todo_list()
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num - 1)

        with open("todo_list.txt", "w") as file:
            file.writelines(tasks)

        print(f"❌ Removed: {removed.strip()}")
    except (FileNotFoundError, ValueError, IndexError):
        print("⚠️ Invalid input or file not found!")


# --- Main Program ---
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        view_todo_list()
    elif choice == "2":
        add_todo_item()
    elif choice == "3":
        remove_todo_item()
    elif choice == "4":
        print("👋 Exiting To-Do App. Goodbye!")
        break
    else:
        print("⚠️ Invalid option! Try again.")
