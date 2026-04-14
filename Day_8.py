tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        print("Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

    elif choice == "3":
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            tasks.pop(index - 1)
        else:
            print("Invalid task number")

    elif choice == "4":
        break

    else:
        print("Invalid choice")

print("\nFinal Task List:")
if tasks:
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")
else:
    print("No tasks available")