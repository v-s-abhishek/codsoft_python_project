import pickle
import os

TASKS_FILE = 'tasks.pkl'

def load_tasks():
    """Load tasks from file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'rb') as file:
            return pickle.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, 'wb') as file:
        pickle.dump(tasks, file)

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ")
    tasks.append({'task': task, 'completed': False})

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks to show.")
    for index, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{index + 1}. {task['task']} - {status}")

def update_task(tasks):
    """Update a task's completion status."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = not tasks[task_num]['completed']
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
