import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Create UI elements
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=5)

        # Initialize the task list
        self.tasks = {}

    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Warning", "You must enter a task.")
            return
        if task in self.tasks:
            messagebox.showinfo("Info", "Task already exists.")
            return
        self.tasks[task] = False
        self.update_listbox()
        self.task_entry.delete(0, tk.END)
        self.status_label.config(text=f"Task '{task}' added.")

    def update_task(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if not selected_task:
            messagebox.showwarning("Warning", "You must select a task.")
            return
        # Remove status symbol to get the task name
        task_name = selected_task[2:].strip()  # Remove '✔ ' or '✘ ' from the beginning
        new_task = self.task_entry.get().strip()
        if not new_task:
            messagebox.showwarning("Warning", "You must enter a new task.")
            return
        if new_task in self.tasks and new_task != task_name:
            messagebox.showinfo("Info", "Task already exists.")
            return
        # Remove the old task and add the updated task
        self.tasks[new_task] = self.tasks.pop(task_name)
        self.update_listbox()
        self.task_entry.delete(0, tk.END)
        self.status_label.config(text=f"Task '{task_name}' updated to '{new_task}'.")

    def delete_task(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if not selected_task:
            messagebox.showwarning("Warning", "You must select a task.")
            return
        # Remove status symbol to get the task name
        task_name = selected_task[2:].strip()  # Remove '✔ ' or '✘ ' from the beginning
        if task_name in self.tasks:
            del self.tasks[task_name]
            self.update_listbox()
            self.status_label.config(text=f"Task '{task_name}' deleted.")
        else:
            messagebox.showwarning("Warning", "Task not found.")

    def mark_completed(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if not selected_task:
            messagebox.showwarning("Warning", "You must select a task.")
            return
        # Remove status symbol to get the task name
        task_name = selected_task[2:].strip()  # Remove '✔ ' or '✘ ' from the beginning
        if task_name in self.tasks:
            self.tasks[task_name] = not self.tasks[task_name]
            self.update_listbox()
            status = "completed" if self.tasks[task_name] else "incomplete"
            self.status_label.config(text=f"Task '{task_name}' marked as {status}.")
        else:
            messagebox.showwarning("Warning", "Task not found.")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task, completed in self.tasks.items():
            status = "✔" if completed else "✘"
            self.tasks_listbox.insert(tk.END, f"{status} {task}")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
