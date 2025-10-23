todos = []

while True:
    print("\n--- TODO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        task = input("Enter a task: ")
        todos.append(task)
        print(f"Added: {task}")
    
    elif choice == "2":
        if todos:
            print("\nYour tasks:")
            for i, task in enumerate(todos, 1):
                print(f"  {i}. {task}")
        else:
            print("No tasks yet!")
    
    elif choice == "3":
        if todos:
            for i, task in enumerate(todos, 1):
                print(f"  {i}. {task}")
            num = int(input("Remove which task? (number): "))
            if 0 < num <= len(todos):
                removed = todos.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number!")
        else:
            print("No tasks to remove!")
    
    elif choice == "4":
        print("Bye!")
        break
    
    else:
        print("Invalid choice!")
