
def load_tasks():
    try:
        
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
           
            tasks = [task.strip() for task in tasks]
        return tasks
    except FileNotFoundError:
      
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
       
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks(tasks):
    print("\n--- Your Task List ---")
    if not tasks:
        print("📂 No tasks found!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("\nEnter the task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f"❌ Task '{removed}' removed successfully!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
   
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("💾 Exiting... Tasks saved in 'tasks.txt'. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
