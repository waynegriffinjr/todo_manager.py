# todo_manager.py - A simple interactive to-do list.

# Header
print("=" * 35)
print("           My To-Do List")
print("=" * 35)

# Current To-do List
tasks = ["kroger", "homework", "mow"]

#Display a vertical numbered list
for i, task in enumerate(tasks, start=1):   # Loop that numbers the list and
    print(f"{i}. {task}")                   # unpacks it in one step to print cleanly

# Total number of tasks
num_tasks = len(tasks)
print(f"\nTotal tasks: {num_tasks}")

# Allow user to add or remove a task from their list
try:
    choice = int(input("\nWhat would you like to do?: Enter 1 for Add Task or 2 To-Remove Task: ")) 
except ValueError:                                   # Error Handling that defaults to continue 
    print("\nInvalid entry. Add Task selected.")
    choice = 1
    
if choice == 1:                             # User selects 1, enters next to-do, and then adds to list 
    new_task = (input("\nNew task: "))
    print("\nAdded to your to-do list!")
    tasks.append(new_task)

    for i, task in enumerate(tasks, start=1): # makes a numbered list where i = # and task = to-do
        print(f"{i}. {task}")                 # prints the entire list numbered starting with 1    

elif choice == 2:
    try:
        done_task = int(input("\nEnter completed task number: ")) # gets index value of user input 
        index = done_task - 1   # reconciles for python base 10 (0,1,2)
        completed = tasks.pop(index) # removes indexed task from list
        print(f"\nRemoved {completed} from your to-do list!") # confirms completion/removal to the user
        for i, task in enumerate(tasks, start=1):
         print(f"{i}. {task}")
    except IndexError:
       print("Invalid entry. Please run the program again and enter 1 or 2.")   #error handling 
else:
    print("Invalid entry. Please run the program again and enter 1 or 2.")

       
 
    
# Future additon loop: fix_choice = input("Invalid entry." Please enter 1 or 2: ")"
