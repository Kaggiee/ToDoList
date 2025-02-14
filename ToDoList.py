"""
A simple to-do list application that allows users to add, remove, and view tasks.
Requirements:
- Store tasks in a list
- Allow users to add tasks
- Allow users to remove tasks
- Display the task list
- Save tasks to a file so they persist between runs (optional)
"""
import os

# File to store tasks
FILE_NAME = "todolist.txt"

# Load tasks from file
def load_tasks():
    # Check if file exists before reading
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in task_list:
            file.write(task + "\n")

# Print tasks
def print_list():
    if task_list == []:
        print("\nYou have no tasks.")
    else:
        print("\nTo-Do List\n")
        for i, task in enumerate(task_list):
            print(f"{i+1}. {task}")

task_list = load_tasks()
run = True

# Get user choice
print("What do you want to do?")

while run == True:
    # Choices
    print("\n1. Add a new task")
    print("2. Remove a task")
    print("3. View list")
    print("4. Exit")

    try:
        choice = int(input("Enter a number to choose: "))
    except ValueError:
        print("\nPlease enter a valid number!")
    else:
        # Get new task
        if (choice == 1):
            new_task = input("Enter a new task: ")
            task_list.append(new_task)
            save_tasks()
            print("Task added!")
            print_list()

        # Remove a task
        elif (choice == 2):
            print_list()
            try:
                # Skip loop if list is empty
                if task_list == []:
                    continue
                # Get task to remove
                removed_task = int(input("\nEnter the number of the task to remove: "))
                if 1 <= removed_task <= len(task_list):
                    # Remove task indexed 1 above 0
                    task_list.pop(removed_task - 1)
                    save_tasks()
                    print("Task removed!")
                    print_list()
                else:
                    # Handle if user inputs a task that does not exist
                    print("\nInvalid task number!")
            except ValueError:
                print("\nPlease enter a valid number!")

        # View list
        elif (choice == 3):
            print_list()

        # Quit program
        else:
            run = False