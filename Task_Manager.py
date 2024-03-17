import json
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        task['created_at'] = str(datetime.now())
        self.tasks.append(task)
        print(f"Task '{task['title']}' added successfully!")

    def mark_task(self, task_index):
        try:
            task = self.tasks[task_index]
            task['completed'] = True
            print(f"Task '{task['title']}' marked as completed!")
        except IndexError:
            print("Invalid task index. Please check the index and try again.")

    def delete_task(self, task_index):
        try:
            deleted_task = self.tasks.pop(task_index)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        except IndexError:
            print("Invalid task index. Please check the index and try again.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.get('completed', False) else "Pending"
                print(f"{i + 1}. {task['title']} - {status}")

    def save_tasks(self, filename='tasks.json'):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)
        print(f"Tasks saved to {filename}.")

    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
            print(f"Tasks loaded from {filename}.")
        except FileNotFoundError:
            print(f"No tasks found in {filename}.")

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: (x.get('completed', False), x['created_at']))

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Sort Tasks")
        print("8. Quit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            title = input("Enter task title: ")
            task_manager.add_task({'title': title})
        elif choice == '2':
            task_manager.view_tasks()
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            task_manager.mark_task(task_index)
        elif choice == '3':
            task_manager.view_tasks()
            task_index = int(input("Enter task index to delete: ")) - 1
            task_manager.delete_task(task_index)
        elif choice == '4':
            task_manager.view_tasks()
        elif choice == '5':
            task_manager.save_tasks()
        elif choice == '6':
            task_manager.load_tasks()
        elif choice == '7':
            task_manager.sort_tasks()
            task_manager.view_tasks()
        elif choice == '8':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
