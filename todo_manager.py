# todo_manager.py - A simple interactive to-do list.

# Header
print("=" * 35)
print("           My To-Do List")
print("=" * 35)

# Current To-do List
tasks = ["kroger", "homework", "mow"]

#Display a vertical numbered list
for i, task in enumerate(tasks, start=1):   # Loop that numbers the list and unpacks
    print(f"{i}. {task}")                   # it in one step to print cleanly

# Total number of tasks
num_tasks = len(tasks)
print(f"\nTotal tasks: {num_tasks}")

# Allow user to add or remove a task from their list
try:
    choice = int(input("\nWhat would you like to do?: Enter 1 for Add Task or 2 To-Remove Task: ")) 
except ValueError:
    print("\nInvalid entry. Add Task selected.")
    choice = 1
    
if choice == 1:
    new_task = (input("\nNew task: "))
    print("\nAdded to your to-do list!")
    tasks.append(new_task)

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

elif choice == 2:
    try:
        done_task = int(input("\nEnter completed task number: "))
        index = done_task - 1
        completed = tasks.pop(index)
        print(f"\nRemoved {completed} from your to-do list!")
        for i, task in enumerate(tasks, start=1):
         print(f"{i}. {task}")
    except IndexError:
       print("Invalid entry. Please run the program again and enter 1 or 2.")   
else:
    print("Invalid entry. Please run the program again and enter 1 or 2.")

       
 
    
# Future additon loop: fix_choice = input("Invalid entry." Please enter 1 or 2: ")"