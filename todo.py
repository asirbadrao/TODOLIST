import sys
tasks = []

def add_task(description):
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'completed': False
    }
    tasks.append(task)
    print(f"Task added: {description}")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = "Done" if task['completed'] else "Not Done"
            print(f"{task['id']}. {task['description']} - {status}")

def mark_task_complete(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"Task {task_id} marked as complete.")
            return
    print(f"Task {task_id} not found.")

def remove_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task {task_id} removed.")

def update_task(task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            print(f"Task {task_id} updated to: {new_description}")
            return
    print(f"Task {task_id} not found.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Update Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_complete(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to remove: "))
            remove_task(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            update_task(task_id, new_description)
        elif choice == '6':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
