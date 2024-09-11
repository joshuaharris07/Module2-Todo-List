def add_task(task_name, status = "incomplete"):
    pass

def view_tasks():
    pass

def complete_task():
    pass

def delete_task():
    pass

print("Welcome to the To-Do List App!")
while True:
    menu_action = input("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit\n")
    if menu_action == "1":
        add_task()
    elif menu_action == "2":
        view_tasks()
    elif menu_action == "3":
        complete_task()
    elif menu_action == "4":
        delete_task()
    elif menu_action == "5":
        print("Thank you for using the To-Do List App! Have a great day!")
        break
    else:
        print("Invalid input. Please enter 1, 2, 3, 4, or 5 to make your selection.")