# Simple To-Do List Application

def show_tasks(tasks):
    """Displays the list of tasks."""
    if not tasks:
        print("\nNo tasks to show. Your list is empty!\n")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Pending"
            print(f"{idx}. {task['task']} - [{status}]")
        print()  # for spacing

def add_task(tasks):
    """Adds a new task to the list."""
    task_name = input("\nEnter the task description: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' has been added!\n")

def mark_completed(tasks):
    """Marks a task as completed."""
    show_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def main():
    tasks = []
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.\n")

if __name__ == "__main__":
    main()
