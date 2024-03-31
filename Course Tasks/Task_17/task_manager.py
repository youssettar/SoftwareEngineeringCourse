# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data 
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
curr_user = ""

def display_menu():
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    return input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
e - Exit
: ''').lower()

def reg_user():
    new_username = input("New Username: ")

    # Check if the username already exist 
    if new_username in username_password.keys():
        print("Username already exists. Please choose a different username.")
        return 
    
    new_password = input("New Password: ")
    confirm_password = input("Confirm password: ")

    if new_password == confirm_password:
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "a") as out_file:
            out_file.write(f"\n{new_username};{new_password}")

    else:
        print("Passwords do not match")

def add_task():
    task_username = input("Name of person assigned to task: ")

    if task_username not in username.password.keys():
        print("User does not exist. Please enter a valid username.")
        return
    
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True: 
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strip.time(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    curr_date = date.today()

    new_task = {
        "username": task_username, 
        "title": task_title,
        "description": task_description,
        "due date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("task.txt", "a") as task_file:
        task_file.write(f"\n{new_task['username']};{new_task['title']};{new_task['description']};{new_task['due_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if new_task['completed'] else 'No'}")
    print("Task successfully added.")


    # elif menu == 'va':
    #     '''Reads the task from task.txt file and prints to the console in the 
    #        format of Output 2 presented in the task pdf (i.e. includes spacing
    #        and labelling) 
    #     '''

def view_all():
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

def view_mine():
    print("Tasks assigned to you:")
    for i, t in enumerate(task_list, start=1):
         disp_str = f"Task: \t\t {t['title']}\n"
         disp_str += f"Assigned to: \t {t['username']}\n"
         disp_str += f"Date assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
         disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
         disp_str += f"Task Description: \n {t['description']}\n"
         print(disp_str)

    task_number = int(input("Enter the number of the task you want to select (enter -1 to return to the main menu): "))

    if task_number == -1:
        return
    if 1 <= task_number <= len(task_list):
        selected_task = task_list[task_number - 1]

        if selected_task['completed']:
            print("This task has already been completed and cannot be edited.")
        else:
            print("\nSelected Task:")
            print(f"Task: \t\t {selected_task['title']}")
            print(f"Assigned to: \t {selected_task['username']}")
            print(f"Date Assigned: \t {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Due Date: \t {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Task Description: \n {selected_task['description']}")
            print(f"Completed: \t {selected_task['completed']}")

            action = input("Choose an action:\n1. Mark as Complete\n2. Edit Task\nEnter your choice (1/2): ")

            if action == '1':
                selected_task['completed'] = True 
                print("Task marked as complete.")
            elif action == '2':
                if not selected_task['completed']:
                    new_username = input("Enter new username for the task: ")
                    selected_task['username'] = new_username

                    while True:
                        try:
                            new_due_date = input("Enter new due date for the task (YYYY-MM-DD): ")
                            selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                            break
                        except ValueError:
                            print("Invalid datetime format. Please use format specified.")
                    print("Task edited successfully.")
                else:
                    print("This task has already been completed and cannot be edited.")
            else:
                print("Invalid choice. Returning to the main menu.")
    else:
        print("Invalid task number. Returning to main menu.")
                    
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")

    if curr_user not in username_password.keys():
        print("User does not exist")
        continue 
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login successful!")
        logged_in = True 

# Main loop
while True:
    menu = display_menu()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    
    # Add other menu options and corresponding function calls as needed 
    elif menu == 'ds' and curr_user == 'admin':
        num_users = len(username_password.key())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
    