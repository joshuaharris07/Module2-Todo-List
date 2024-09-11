def add_task(task_name, status = "Incomplete"):
    if len(task_name.strip()) < 1:
        print("No task was entered, returning to the menu.")
    elif [task_name, status] in task_list:
        print(f"That task is already in your to-do list and is currently {status}.")
    else:
        new_task = [task_name, status]
        task_list.append(new_task)

def view_tasks():
    for task in task_list:
        print(f"{task[0]} is {task[1]}")

def complete_task(completed_task):
    try:
        task_list.remove([completed_task, "Incomplete"])
    except:
        print(f"{completed_task} is not in your Todo list.")
    else:
        print(f"{completed_task} has been marked complete.")
        finished_tasks.append(completed_task)
    finally:
        print("Returning to the menu.")

def delete_task(task_to_delete):
    try:
        task_list.remove([task_to_delete, "Incomplete"])
    except:
        print(f"{task_to_delete} is not in your Todo list.")
    else:
        print(f"{task_to_delete} has been deleted from the Todo list.")
    finally:
        print("Returning to the menu.")

def view_finished_tasks():
    print("Here is your list of tasks you have completed:")
    for task in finished_tasks:
        print(f"{task}")

task_list = [["Water plants", "Incomplete"], ["Eating", "Incomplete"], ["Read a book", "Incomplete"]] #empty before finalizing? maybe leave
finished_tasks = ["Shopping"]

print("Welcome to the To-Do List App!\n")

while True:
    welcome = "Menu"
    print(welcome.center(20, "*"))
    menu_action = input("\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. View completed tasks\n6. Quit\n")
    if menu_action == "1":
        task_name = input("Please input a name for the task: ").capitalize()
        add_task(task_name)
    elif menu_action == "2":
        view_tasks()
    elif menu_action == "3":
        completed_task = input("Which task have you completed: ").capitalize()
        if len(completed_task.strip()) < 1:
            print("No task was entered, returning to the menu.")
        else:
            complete_task(completed_task)
    elif menu_action == "4":
        task_to_delete = input("Which task would you like to delete? Please type the name: ").capitalize()
        if len(task_to_delete.strip()) < 1:
            print("No task was entered, returning to the menu.")
        else:
            delete_task(task_to_delete)
    elif menu_action == "5":
        view_finished_tasks()
    elif menu_action == "6":
        print("Thank you for using the To-Do List App! Have a great day!")
        break
    else:
        print("Invalid input. Please enter 1, 2, 3, 4, or 5 to make your selection.\n")