# todo.py

import os

TASK_FILE = "tasks.txt"

# Load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("||")
                tasks.append({"task": task, "done": status == "1"})
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            status = "1" if task["done"] else "0"
            file.write(f"{task['task']}||{status}\n")

# Display all tasks
def view_tasks(tasks):
    print("\n📋 Your Tasks:")
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task_text = input("Enter a new task: ").strip()
    if not task_text:
        print("⚠️ Task cannot be empty.")
        return
    tasks.append({"task": task_text, "done": False})
    print("✅ Task added.")

# Remove a task by number
def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Removed: {removed['task']}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Mark a task as completed
def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter the task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(f"🎉 Task marked as completed: {tasks[num - 1]['task']}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Show the main menu
def show_menu():
    print("\n📌 To-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

# Main app loop
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_done(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
