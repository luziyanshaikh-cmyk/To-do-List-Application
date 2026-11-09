
FILE_NAME = "tasks.txt"



def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []



def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    task = input("Enter your task: ").strip()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")



def view_tasks(tasks):
    print("\n------ YOUR TO-DO LIST ------")

    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def remove_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")



def main():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST APPLICATION ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("Thank you for using To-Do List Application!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
