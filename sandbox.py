# Trying idea of adding the functions to a list and calling them that way. 
# Looks like I may be able to do it but would require some re-writing of the code.

# def add_task(task_name, status = "Incomplete"):
#     if [task_name, status]  in task_list:
#         print(f"That task is already in your to-do list and is currently {status}.")
#     else:
#         new_task = [task_name, status]
#         task_list.append(new_task)

# def view_tasks():
#     for task in task_list:
#         print(f"{task[0]} is {task[1]}")

# def complete_task(completed_task):
#     if [completed_task, "Incomplete"] in task_list:
#         task_list.remove([completed_task, "Incomplete"])
#         print(f"{completed_task} has been marked complete.")
#         finished_tasks.append(completed_task)
#         print(f"Finished tasks: {finished_tasks}")

# def delete_task(task_to_delete):
#     try:
#         task_list.remove([task_to_delete, "Incomplete"])
#     except:
#         print(f"{task_to_delete} is not in your Todo list.")
#     else:
#         print(f"{task_to_delete} has been deleted from the Todo list.")
#     finally:
#         print("Returning to the menu.")

# def view_finished_tasks():
#     print("Here is your list of tasks you have completed:")
#     for task in finished_tasks:
#         print(f"{task}")

# task_list = [["Water plants", "Incomplete"], ["Eating", "Incomplete"], ["Read a book", "Incomplete"]] #empty before finalizing
# finished_tasks = ["Shopping"]
# menu_action_list = [add_task, view_tasks]

# print("Welcome to the To-Do List App!\n")
# while True:
#     menu_action = int(input("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. View completed tasks\n6. Quit\n"))
#     menu_action_list[menu_action-1]()