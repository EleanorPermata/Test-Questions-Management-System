# IMPORTING LIBRARIES
import os  # Importing the os module for interacting with the operating system
import sys  # Importing the sys module for accessing system-specific parameters and functions
import json  # Importing the json module for working with JSON data
import getpass  # Importing the getpass module to securely prompt the user for a password

current_ad = None  # Initializing a variable to store the currently logged-in Administrator (set to None initially)
current_lect = None  # Initializing a variable to store the currently logged-in Lecturer (set to None initially)
current_examp = None  # Initializing a variable to store the currently logged-in Exam Unit Personnel (set to None initially)

# CLEAR PREVIOUS DIALOGUE FUNCTION
def clr():
    os.system('cls')  # Defining a function 'clr()' to clear the console screen using the 'cls' command on Windows systems


#__________________________________________________________________________________________________________________________________________________________#
# MAIN MENU

# MAIN MENU
def menu():
  while True:  # Entering an infinite loop for the main menu to continuously prompt the user until an exit choice is selected
    print("[MANAGEMENT SYSTEM MAIN MENU]")
    print("1. SIGN-UP ADMIN ACCOUNT")
    print("2. SIGN-IN MENU")
    print("3. Exit the app")

    try:
      choice = int(input("\nEnter your choice (1-3): "))  # Prompting the user to enter a choice (1-3) and converting the input to an integer

      if choice == 1:
        clr()  # Clearing the console screen
        admin_signup()  # Calling a function to handle the sign-up process for an admin account
      elif choice == 2:
        clr()  # Clearing the console screen
        sign_in_menu()  # Calling a function to handle the sign-in menu
      elif choice == 3:
        print("\nProgram will now exit.\n")  # Displaying a message indicating the program will exit
        raise SystemExit  # Raising SystemExit to terminate the program
      else:
        clr()  # Clearing the console screen
        print("Invalid choice, please enter a number between 1 and 3.\n")  # Displaying a message for an invalid choice

    except ValueError:
      clr()  # Clearing the console screen
      print("Invalid input, please enter a number.\n")  # Displaying a message for an invalid input (non-numeric)




#__________________________________________________________________________________________________________________________________________________________#
# 1. SING-UP ADMIN ACCOUNT
#__________________________________________________________________________________________________________________________________________________________#

# Function to add a new admin account
def admin_signup():
    print("[SIGN-UP ADMIN ACCOUNT]\n")
    # Get admin details from user input
    admin_username = input("\033[91mEnter Admin Username: \033[0m")  # Prompting the user to enter the admin username with colored text
    admin_password = input("\033[91mEnter Admin Password: \033[0m")  # Prompting the user to enter the admin password with colored text

    # Check if any input is null or empty
    if not (admin_username and admin_password):
        input("\nError: Username and password cannot be empty.\nPress enter to return...")  # Displaying an error message if either username or password is empty
        clr()  # Clearing the console screen
        return

    # Create a string with admin information
    admin_info = (
        f"Username: {admin_username}\n"
        f"Password: {admin_password}\n"
    )

    # Open the file in append mode and write admin information
    with open("admin_accounts.txt", "a") as file:  # Opening a file named "admin_accounts.txt" in append mode
        file.write(admin_info + "\n")  # Writing admin information to the file with a newline
        print("\nAdmin account created successfully.")  # Displaying a success message
        input("Press enter to continue...")  # Waiting for the user to press enter before continuing
        clr()  # Clearing the console screen

#__________________________________________________________________________________________________________________________________________________________#
# 2. SIGN-IN MENU
#__________________________________________________________________________________________________________________________________________________________#

# Function to sign in as admin with a maximum of 3 attempts
def sign_in_menu():
  while True:  # Entering an infinite loop for the sign-in menu to continuously prompt the user until they choose to return
    print("[SIGN-IN MENU]")
    print("1. ADMIN SIGN-IN")
    print("2. LECTURER SIGN-IN")
    print("3. EXAM UNIT PERSONNEL SIGN-IN")
    print("4. RETURN TO MAIN MENU")

    try:
      choice = int(input("\nEnter your choice (1-4): "))  # Prompting the user to enter a choice (1-4) and converting the input to an integer

      if choice == 1:
        clr()  # Clearing the console screen
        admin_signin()  # Calling a function to handle the admin sign-in process
      elif choice == 2:
        clr()  # Clearing the console screen
        lect_signin()  # Calling a function to handle the lecturer sign-in process
      elif choice == 3:
        clr()  # Clearing the console screen
        examp_signin()  # Calling a function to handle the exam unit personnel sign-in process
      elif choice == 4:
        clr()  # Clearing the console screen
        menu()  # Calling the main menu function to return to the main menu
      else:
        clr()  # Clearing the console screen
        print("Invalid choice, please enter a number between 1 and 4.\n")  # Displaying a message for an invalid choice

    except ValueError:
      clr()  # Clearing the console screen
      print("Invalid input, please enter a number.\n")  # Displaying a message for an invalid input (non-numeric)











#__________________________________________________________________________________________________________________________________________________________#
# 2.1. ADMIN SIGN-IN
#__________________________________________________________________________________________________________________________________________________________#

# Function to sign in as admin with a maximum of 3 attempts
def admin_signin():

  global current_ad  # Declaring a global variable to store the currently logged-in admin

  try:
  
    # Read existing admin accounts from the file
    with open("admin_accounts.txt", "r") as file:  # Opening the file "admin_accounts.txt" in read mode
      admin_accounts = file.read().strip().split("\n\n")  # Reading and splitting the file content into admin accounts based on double newline characters

    max_attempts = 3  # Setting the maximum number of sign-in attempts
    for attempt in range(1, max_attempts + 1):  # Iterating through the allowed sign-in attempts
      print("[ADMIN SIGN-IN]\n")
      entered_username = input("Enter Admin Username: ")  # Prompting the user to enter the admin username
      entered_password = input("Enter Admin Password: ")  # Prompting the user to enter the admin password

      # Check if the entered username and password match any admin account
      for admin_account in admin_accounts:
        stored_username = admin_account.split("\n")[0].split(":")[1].strip()  # Extracting the stored admin username from the file
        stored_password = admin_account.split("\n")[1].split(":")[1].strip()  # Extracting the stored admin password from the file

        if entered_username == stored_username and entered_password == stored_password:
          clr()  # Clearing the console screen
          current_ad = stored_username  # Updating the currently logged-in admin
          admin_menu()  # Calling a function to handle the admin menu

      attempts = max_attempts - attempt

      if attempts > 0:
        input(f"\nSorry, your login attempt was unsuccessful. You have {attempts} attempt(s) remaining.\nPress enter to continue...")
        clr()  # Clearing the console screen
      else:
        input(f"\nSorry, you have reached the login attempts. Exiting program due to multiple failed attempts.\nPress enter to continue...")
        clr()  # Clearing the console screen

    raise SystemExit  # Raising SystemExit to terminate the program after multiple failed attempts
  
  except FileNotFoundError:
    input(f"[FATAL ERROR]\nFile 'admin_accounts.txt' not found. Please sign-up an admin account to create the file.\nPress enter to continue...")
    clr()  # Clearing the console screen

#__________________________________________________________________________________________________________________________________________________________#
# 2.2. LECTURER SIGN-IN
#__________________________________________________________________________________________________________________________________________________________#

def lect_signin():
  # Declaring current_lect as a global variable to be accessible outside the function
  global current_lect

  # Read existing lecturer accounts from the file
  with open("lecturer_accounts.txt", "r") as file:  # Opening the file "lecturer_accounts.txt" in read mode
    lecturer_accounts = file.read().strip().split("\n\n")  # Reading and splitting the file content into lecturer accounts based on double newline characters

  max_attempts = 3  # Setting the maximum number of sign-in attempts
  for attempt in range(1, max_attempts + 1):  # Iterating through the allowed sign-in attempts
    print("[LECTURER SIGN-IN]\n")
    entered_username = input("Enter Lecturer Username: ")  # Prompting the user to enter the lecturer username
    entered_password = input("Enter Lecturer Password: ")  # Prompting the user to enter the lecturer password

    for lecturer_account in lecturer_accounts:
      stored_username = lecturer_account.split("\n")[8].split(":")[1].strip()  # Extracting the stored lecturer username from the file
      stored_password = lecturer_account.split("\n")[9].split(":")[1].strip()  # Extracting the stored lecturer password from the file
          
      if entered_username == stored_username and entered_password == stored_password:
        clr()  # Clearing the console screen
        # Setting the current_user variable to the entered username
        current_lect = stored_username  # Updating the currently logged-in lecturer
        lect_menu()  # Calling a function to handle the lecturer menu

        # Returning True to indicate successful login
        return True
      
    attempts = max_attempts - attempt

    if attempts > 0:
      input(f"\nSorry, your login attempt was unsuccessful. You have {attempts} attempt(s) remaining.\nPress enter to continue...")
      clr()  # Clearing the console screen
    else:
      input(f"\nSorry, you have reached the login attempts. Exiting program due to multiple failed attempts.\nPress enter to continue...")
      clr()  # Clearing the console screen

  raise SystemExit  # Raising SystemExit to terminate the program after multiple failed attempts

#__________________________________________________________________________________________________________________________________________________________#
# 2.3. EXAM UNIT PERSONNEL SIGN-IN
#__________________________________________________________________________________________________________________________________________________________#

def examp_signin():
  # Declaring current_examp as a global variable to be accessible outside the function
  global current_examp

  # Read existing exam unit personnel accounts from the file
  with open("exam_personnel_accounts.txt", "r") as file:  # Opening the file "exam_personnel_accounts.txt" in read mode
    examp_accounts = file.read().strip().split("\n\n")  # Reading and splitting the file content into exam unit personnel accounts based on double newline characters

  max_attempts = 3  # Setting the maximum number of sign-in attempts
  for attempt in range(1, max_attempts + 1):  # Iterating through the allowed sign-in attempts
    print("[EXAM UNIT PERSONNEL SIGN-IN]\n")
    entered_username = input("Enter Exam Unit Personnel Username: ")  # Prompting the user to enter the exam unit personnel username
    entered_password = input("Enter Exam Unit Personnel Password: ")  # Prompting the user to enter the exam unit personnel password

    for examp_account in examp_accounts:
      stored_username = examp_account.split("\n")[0].split(":")[1].strip()  # Extracting the stored exam unit personnel username from the file
      stored_password = examp_account.split("\n")[1].split(":")[1].strip()  # Extracting the stored exam unit personnel password from the file
          
      if entered_username == stored_username and entered_password == stored_password:
        clr()  # Clearing the console screen
        # Setting the current_examp variable to the entered username
        current_examp = stored_username  # Updating the currently logged-in exam unit personnel
        examp_menu()  # Calling a function to handle the exam unit personnel menu

        # Returning True to indicate successful login
        return True

    attempts = max_attempts - attempt

    if attempts > 0:
      input(f"\nSorry, your login attempt was unsuccessful. You have {attempts} attempt(s) remaining.\nPress enter to continue...")
      clr()  # Clearing the console screen
    else:
      input(f"\nSorry, you have reached the login attempts. Exiting program due to multiple failed attempts.\nPress enter to continue...")
      clr()  # Clearing the console screen

  raise SystemExit  # Raising SystemExit to terminate the program after multiple failed attempts











#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1. ADMIN MENU

def admin_menu():
  while True:  # Entering an infinite loop for the admin menu to continuously prompt the user until they choose to sign out
    print(f"Welcome, Admin {current_ad}!\n")  # Displaying a welcome message with the current admin's username
    print("[ADMIN MENU]")
    print("1. LECTURER SETTINGS")
    print("2. EXAM UNIT PERSONNEL SETTINGS")
    print("3. SUBJECTS AND TOPICS SETTINGS")
    print("4. SIGN-OUT")

    try:
      choice = int(input("\nEnter your choice (1-4): "))  # Prompting the user to enter a choice (1-4) and converting the input to an integer

      if choice == 1:
        clr()  # Clearing the console screen
        adm_lec_st()  # Calling a function to handle the admin lecturer settings
        sign_in_menu()  # Returning to the sign-in menu after lecturer settings are complete
      elif choice == 2:
        clr()  # Clearing the console screen
        adm_examp_st()  # Calling a function to handle the admin exam unit personnel settings
        sign_in_menu()  # Returning to the sign-in menu after exam unit personnel settings are complete
      elif choice == 3:
        clr()  # Clearing the console screen
        adm_sat_st()  # Calling a function to handle the admin subjects and topics settings
        sign_in_menu()  # Returning to the sign-in menu after subjects and topics settings are complete
      elif choice == 4:
        clr()  # Clearing the console screen
        sign_in_menu()  # Returning to the sign-in menu
      else:
        clr()  # Clearing the console screen
        print("Invalid choice, please enter a number between 1 and 3.\n")  # Displaying a message for an invalid choice

    except ValueError:
      clr()  # Clearing the console screen
      print("Invalid input, please enter a number.\n")  # Displaying a message for an invalid input (non-numeric)











#__________________________________________________________________________________________________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1.1. LECTURER SETTINGS

# Lecturer Settings main menu loop
def adm_lec_st():
  while True:  # Entering an infinite loop for the lecturer settings menu to continuously prompt the user until they choose to go back
    print("[LECTURER SETTINGS]")
    print("1. CREATE LECTURER ACCOUNT")
    print("2. MODIFY LECTURER PROFILE")
    print("3. DELETE LECTURER ACCOUNT")
    print("4. BACK TO ADMIN MENU")

    # Get user choice
    try:
      choice = int(input("\nEnter your choice (1-4): "))  # Prompting the user to enter a choice (1-4) and converting the input to an integer
      clr()  # Clearing the console screen

      if choice == 1:     # Call function to add lecturer account
        lect_add_acc()  # Calling a function to handle the addition of a lecturer account
        clr()  # Clearing the console screen
      elif choice == 2:   # Call function to edit lecturer account
        lect_edt_acc()  # Calling a function to handle the editing of a lecturer account
        clr()  # Clearing the console screen
      elif choice == 3:   # Call function to delete lecturer account
        lect_del_acc()  # Calling a function to handle the deletion of a lecturer account
        clr()  # Clearing the console screen
      elif choice == 4:
        admin_menu()  # Returning to the admin menu
      else:
        clr()  # Clearing the console screen
        print("Invalid choice, please enter a number between 1 and 4.\n")  # Displaying a message for an invalid choice

    except ValueError:
      clr()  # Clearing the console screen
      print("Invalid input, please enter a number.\n")  # Displaying a message for an invalid input (non-numeric)


#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1.1.1. CREATE LECTURER ACCOUNT

# Function to add a new lecturer account
def lect_add_acc():
    # Get lecturer details from user input
    print("[SIGN-UP LECTURER ACCOUNT]\n")
    lecturer_name = input("Name: ")
    lecturer_address = input("Address: ")
    lecturer_contact = input("Contact Number: ")
    lecturer_dob = input("Enter Date of Birth (dd/mm/yyyy): ")
    lecturer_email = input("E-mail Address: ")
    lecturer_age = input("Age: ")
    lecturer_citizenship = input("Citizenship: ")
    lecturer_id = input("ID Number: ")
    lecturer_username = input("\n" + "\033[91mUsername: \033[0m")  # Prompting the user for the lecturer's username with red-colored text
    lecturer_password = input("\033[91mPassword: \033[0m")  # Prompting the user for the lecturer's password with red-colored text

    # Check if any input is null or empty
    if (
        not all(
            [
                lecturer_name,
                lecturer_address,
                lecturer_contact,
                lecturer_dob,
                lecturer_email,
                lecturer_age,
                lecturer_citizenship,
                lecturer_id,
                lecturer_username,
                lecturer_password,
            ]
        )
    ):
        input("\nError: All fields must be filled.\nPress enter to continue...")
        clr()  # Clearing the console screen
        return

    # Create a string with lecturer information
    lecturer_info = (
        f"Name: {lecturer_name}\n"
        f"Address: {lecturer_address}\n"
        f"Contact Number: {lecturer_contact}\n"
        f"Date of Birth (dd/mm/yyyy): {lecturer_dob}\n"
        f"E-mail Address: {lecturer_email}\n"
        f"Age: {lecturer_age}\n"
        f"Citizenship: {lecturer_citizenship}\n"
        f"ID Number: {lecturer_id}\n"
        f"Username: {lecturer_username}\n"
        f"Password: {lecturer_password}\n"
    )

    # Open the file in append mode and write lecturer information
    with open("lecturer_accounts.txt", "a") as file:  # Opening the file "lecturer_accounts.txt" in append mode
        file.write(lecturer_info + "\n")  # Writing lecturer information to the file with a newline
        input("\nLecturer account added successfully.\nPress enter to continue...")  # Displaying a success message


#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1.1.2. MODIFY LECTURER PROFILE

def lect_edt_acc():
    # Read existing accounts from the file
    with open("lecturer_accounts.txt", "r") as file:
        accounts = file.read().strip().split("\n\n")

    print("[MODIFY LECTURER ACCOUNT INFO]\n")
    # Display available accounts for editing
    print("Available accounts:")
    for i, account in enumerate(accounts, start=1):
        username = account.split("\n")[8].split(":")[1].strip()  # Extract username
        print(f"{i}. {username}")

    # Get user's choice of account to edit
    choice = input("\nEnter the number of the account to modify: ")
    clr()
    print("[MODIFY LECTURER ACCOUNT INFO]\n")

    # Check if the choice is valid
    if not choice.isdigit() or not (0 < int(choice) <= len(accounts)):
        input("Invalid choice. Please enter a valid number.\nPress enter to return...")
        return

    # Get the selected account details
    selected_account = accounts[int(choice) - 1].split("\n")
    edited_account = accounts[int(choice) - 1].split("\n")[8].split(":")[1].strip()
    # Allow the user to choose which part to edit
    print(f"Choose the part to modify from lecturer account \033[91m{edited_account}\033[0m:")
    print("1. Personal Information")
    print("2. Login Credentials")

    part_choice = input("\nEnter your choice (1-2): ")

    if part_choice == "1":
        clr()
        print(f"[MODIFY LECTURER ACCOUNT \033[91m{edited_account}\033[0m INFO]\n")
        # Edit personal information
        for i in range(0, len(selected_account) - 2):  # Exclude username and password
            field_name, current_value = selected_account[i].split(": ")
            new_value = input(f"Enter new {field_name}: ").strip()

            # Check if the input is not null or empty
            while not new_value:
                print(f"Error: {field_name} cannot be empty.")
                new_value = input(f"Enter new {field_name}: ").strip()

            # Update the account details
            selected_account[i] = f"{field_name}: {new_value}"

    elif part_choice == "2":
        clr()
        print(f"[MODIFY LECTURER ACCOUNT \033[91m{edited_account}\033[0m INFO]\n")
        # Edit login credentials
        for i in range(len(selected_account) - 2, len(selected_account)):
            field_name, current_value = selected_account[i].split(": ")
            new_value = input(f"\033[91mEnter new {field_name}\033[0m: ").strip()

            # Check if the input is not null or empty
            while not new_value:
                print(f"Error: {field_name} cannot be empty.")
                new_value = input(f"\033[91mEnter new {field_name}\033[0m: ").strip()

            # Update the account details
            selected_account[i] = f"{field_name}: {new_value}"

    else:
        input("\nInvalid choice. Please enter a valid number.\nPress enter to return...")
        return

    # Update the accounts list
    accounts[int(choice) - 1] = "\n".join(selected_account)

    # Write the updated accounts back to the file
    with open("lecturer_accounts.txt", "w") as file:
        file.write("\n\n".join(accounts) + "\n\n")

    input("\nLecturer account updated successfully.\nPress enter to return...")

#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1.1.3. DELETE LECTURER ACCOUNT

# Function to delete an existing lecturer account
def lect_del_acc():
    # Read existing accounts from the file
    with open("lecturer_accounts.txt", "r") as file:
        accounts = file.read().strip().split("\n\n")

    # Display available accounts for deletion
    print("[DELETE LECTURER ACCOUNT]\n")
    print("Available accounts for deletion:")
    for i, account in enumerate(accounts, start=1):
        username = account.split("\n")[8].split(":")[1].strip()  # Extract username
        print(f"{i}. {username}")

    # Get user's choice of account to delete
    choice = input("\nEnter the number of the account to delete: ")

    # Check if the choice is valid
    if not choice.isdigit() or not (0 < int(choice) <= len(accounts)):
        clr()
        print("[DELETE LECTURER ACCOUNT]\n")
        input("Invalid choice. Please enter a valid number.\nPress enter to return...")
        return
    
    deleted_username = accounts[int(choice) - 1].split("\n")[8].split(":")[1].strip()
    confirm = input(f"Are you sure you want to delete the lecturer account \033[91m{deleted_username}\033[0m? [Y/N]: ")
    if confirm == "Y" or confirm =="y":
      # Delete the selected account
      deleted_account = accounts.pop(int(choice) - 1)

      # Write the updated accounts back to the file
      with open("lecturer_accounts.txt", "w") as file:
          file.write("\n\n".join(accounts) + "\n\n")

      input("\n" + f"Lecturer account \033[91m{deleted_username}\033[0m has been deleted successfully.\nPress enter to return...")

    elif confirm == "N" or confirm =="n":
      input("\nAccount deletion cancelled.\nPress enter to return...")
      return
    
    else:
      input("\nInvalid input.\nPress enter to return...")
      return

    













#__________________________________________________________________________________________________________________________________________________________# 
#__________________________________________________________________________________________________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1.2. EXAM UNIT PERSONNEL SETTINGS

def adm_examp_st():
  while True:  # Entering an infinite loop for the exam unit personnel settings menu to continuously prompt the user until they choose to go back
    print("[EXAM PERSONNEL SETTINGS]")
    print("1. CREATE EXAM UNIT PERSONNEL ACCOUNT")
    print("2. DELETE EXAM UNIT PERSONNEL ACCOUNT")
    print("3. BACK TO ADMIN MENU")

    try:
      choice = int(input("\nEnter your choice (1-3): "))  # Prompting the user to enter a choice (1-3) and converting the input to an integer

      if choice == 1:
        clr()  # Clearing the console screen
        examp_add_acc()  # Calling a function to handle the addition of an exam unit personnel account
        clr()  # Clearing the console screen
      elif choice == 2:
        clr()  # Clearing the console screen
        examp_del_acc()  # Calling a function to handle the deletion of an exam unit personnel account
        clr()  # Clearing the console screen
      elif choice == 3:
        clr()  # Clearing the console screen
        admin_menu()  # Returning to the admin menu
      else:
        clr()  # Clearing the console screen
        print("Invalid choice, please enter a number between 1 and 3.\n")  # Displaying a message for an invalid choice

    except ValueError:
      clr()  # Clearing the console screen
      print("Invalid input, please enter a number.\n")  # Displaying a message for an invalid input (non-numeric)

#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1.2.1. CREATE EXAM UNIT PERSONNEL ACCOUNT

# Function to add a new exam unit personnel account
def examp_add_acc():
    print("[CREATE EXAM UNIT PERSONNEL ACCOUNT]\n")
    # Get exam personnel details from user input
    exam_username = input("\033[91mEnter Username: \033[0m")  # Prompting the user for the exam unit personnel's username with red-colored text
    exam_password = input("\033[91mEnter Password: \033[0m")  # Prompting the user for the exam unit personnel's password with red-colored text

    # Check if any input is null or empty
    if not (exam_username and exam_password):
        input("Error: Username and password cannot be empty.\nPress enter to return...")
        clr()
        return

    # Create a string with exam personnel information
    exam_personnel_info = (
        f"Username: {exam_username}\n"
        f"Password: {exam_password}\n"
    )

    # Open the file in append mode and write exam personnel information
    with open("exam_personnel_accounts.txt", "a") as file:
        file.write(exam_personnel_info + "\n")
        input("\nExam unit personnel account added successfully.\nPress enter to continue...")

#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1.2.2. DELETE EXAM UNIT PERSONNEL ACCOUNT

# Function to delete an existing exam unit personnel account
def examp_del_acc():
    # Read existing accounts from the file
    with open("exam_personnel_accounts.txt", "r") as file:  # Opening the file "exam_personnel_accounts.txt" in read mode
        accounts = file.read().strip().split("\n\n")  # Reading and splitting the file content into exam unit personnel accounts based on double newline characters

    # Display available accounts for deletion
    print("[DELETE EXAM UNIT PERSONNEL ACCOUNT]\n")
    print("Available accounts for deletion:")
    for i, account in enumerate(accounts, start=1):
        username = account.split("\n")[0].split(":")[1].strip()  # Extracting the username from each account
        print(f"{i}. {username}")

    # Get user's choice of account to delete
    choice = input("\nEnter the number of the account to delete: ")

    # Check if the choice is valid
    if not choice.isdigit() or not (0 < int(choice) <= len(accounts)):
        clr()  # Clearing the console screen
        print("[DELETE EXAM UNIT PERSONNEL ACCOUNT]\n")
        input("Invalid choice. Please enter a valid number.\nPress enter to return...")  # Displaying an error message for an invalid choice
        return
    
    deleted_username = accounts[int(choice) - 1].split("\n")[0].split(":")[1].strip()  # Extracting the username of the account to be deleted
    confirm = input(f"Are you sure you want to delete the exam unit personnel account \033[91m{deleted_username}\033[0m? [Y/N]: ")  # Asking for confirmation to delete the selected account
    if confirm == "Y" or confirm =="y":
      # Delete the selected account
      deleted_account = accounts.pop(int(choice) - 1)

      # Write the updated accounts back to the file
      with open("exam_personnel_accounts.txt", "w") as file:  # Opening the file "exam_personnel_accounts.txt" in write mode
          file.write("\n\n".join(accounts) + "\n\n")  # Writing the updated accounts back to the file with double newline characters

      input("\n" + f"Exam unit personnel account \033[91m{deleted_username}\033[0m has been deleted successfully.\nPress enter to return...")  # Displaying a success message
    elif confirm == "N" or confirm =="n":
      input("\nAccount deletion cancelled.\nPress enter to return...")  # Displaying a message for cancelled deletion
      return
    
    else:
      input("\nInvalid input.\nPress enter to return...")  # Displaying a message for invalid input
      return














#__________________________________________________________________________________________________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1.3. SUBJECT AND TOPICS SETTINGS

def adm_sat_st():
  while True:  # Entering an infinite loop for the subject and topics settings menu to continuously prompt the user until they choose to go back
    print("[SUBJECT AND TOPICS SETTINGS]")
    print("1. ADD SUBJECT AND TOPICS")
    print("2. BACK TO ADMIN MENU")

    try:
      choice = int(input("\nEnter your choice (1-2): "))  # Prompting the user to enter a choice (1-2) and converting the input to an integer

      if choice == 1:
        clr()  # Clearing the console screen
        add_sat()  # Calling a function to handle the addition of a subject and topics
        clr()  # Clearing the console screen
      elif choice == 2:
        clr()  # Clearing the console screen
        admin_menu()  # Returning to the admin menu
      else:
        clr()  # Clearing the console screen
        print("Invalid choice, please enter a number between 1 and 2.\n")  # Displaying a message for an invalid choice

    except ValueError:
      clr()  # Clearing the console screen
      print("Invalid input, please enter a number.\n")  # Displaying a message for an invalid input (non-numeric)


#__________________________________________________________________________________________________________________________________________________________#
# 2.1.1.3.1. ADD SUBJECT AND TOPICS

# Define a function named add_sat
def add_sat():
    # Print a message indicating the beginning of the process to add subjects and topics
    print("[ADD SUBJECTS AND TOPICS]\n")

    try:
        # Ask the user to input the number of subjects to create, ensuring it is at least 3
        num_subjects = int(input("Enter the number of Subjects to create (minimum 3): "))
        if num_subjects < 3:
            # If the input is less than 3, prompt the user to retry and return from the function
            input("\nNumber of subjects should be 3 or more.\nPress enter to retry...")
            return
    except ValueError:
        # If the input is not a valid integer, prompt the user to return and exit the function
        input("\nInvalid input.\nPress enter to return...")
        return

    # Create an empty list to store subjects and topics information
    subjects_and_topics = []

    # Call the 'clr' function (not provided here) to clear the console screen
    clr()

    # Iterate through each subject based on the user input
    for subject_num in range(1, num_subjects + 1):

        # Print a message indicating the current subject being processed
        print("[ADD SUBJECTS AND TOPICS]\n")

        # Ask the user to input the name for the current subject
        subject_name = input(f"Enter the name for Subject {subject_num}: ")
        if not subject_name:
            # If the subject name is empty, prompt the user to return and exit the function
            input("\nError: Subject name cannot be empty.\nPress enter to return...")
            clr()
            return

        try:
            # Ask the user to input the number of topics for the current subject, ensuring it is at least 3
            num_topics = int(input(f"Enter the amount of topics for Subject {subject_num} (minimum 3): "))
            if num_topics < 3:
                # If the input is less than 3, prompt the user to retry and return from the function
                input("\nNumber of topics should be 3 or more.\nPress enter to retry...")
                return
        except ValueError:
            # If the input is not a valid integer, prompt the user to return and exit the function
            input("\nInvalid input.\nPress enter to return...")
            return

        # Create an empty list to store topics for the current subject
        topics_list = []

        # Print a message indicating the current subject and ask the user to input topics
        print(f"\n[SUBJECT {subject_num}]")

        # Iterate through each topic based on the user input
        for topic_num in range(1, num_topics + 1):
            # Ask the user to input the name for the current topic
            topic_name = input(f"Enter Topic {topic_num} for Subject {subject_num}: ")
            if not topic_name:
                # If the topic name is empty, prompt the user to return and exit the function
                input("\nError: Topic name cannot be empty.\nPress enter to return...")
                clr()
                return

            # Add the current topic to the list of topics for the current subject
            topics_list.append(topic_name)

        # Print a success message, wait for user input, and clear the console screen
        print("\nSubjects and Topics added successfully and saved.")
        input("Press enter to return...")
        clr()

        # Add the information for the current subject to the list of subjects and topics
        subjects_and_topics.append({
            "Subject Name": subject_name,
            "Topics": topics_list
        })

    # Define the file path for saving the subjects and topics information
    file_path = "subjects_and_topics.txt"

    # Open the file in append mode and write subjects and topics information
    with open(file_path, "a") as file:
        for subject_info in subjects_and_topics:
            # Write the subject name and associated topics to the file
            file.write(f"[SUBJECT {subject_info['Subject Name']}]:\n")
            for topic in subject_info['Topics']:
                file.write(f"  - {topic}\n")
            file.write("\n")

      
















#__________________________________________________________________________________________________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________#
# 2.2.1. LECTURER MENU

# Define a function named lect_menu
def lect_menu():
  # Create an infinite loop for the lecturer menu
  while True:
    # Print a welcome message for the current lecturer
    print(f"Welcome, Lecturer {current_lect}!\n")
    # Print the options for the lecturer menu
    print("[LECTURER MENU]")
    print("1. MODIFY LECTURER ACCOUNT")
    print("2. ADD QUESTIONS AND ANSWERS")
    print("3. EDIT QUESTIONS AND ANSWERS")
    print("4. VIEW QUESTIONS AND ANSWERS")
    print("5. SIGN-OUT")

    try:
      # Attempt to get the user's choice as an integer
      choice = int(input("\nEnter your choice (1-5): "))

      # Check the user's choice and perform corresponding actions
      if choice == 1:
        # Clear the console screen and call the 'edt_lect' function to modify lecturer account
        clr()
        edt_lect()
      elif choice == 2:
        # Clear the console screen and call the 'add_questions' function to add questions and answers
        clr()
        add_questions()
      elif choice == 3:
        # Clear the console screen and call the 'edt_questions' function to edit questions and answers
        clr()
        edt_questions()
      elif choice == 4:
        # Clear the console screen and call the 'view_questions' function to view questions and answers
        clr()
        view_questions()
      elif choice == 5:
        # Clear the console screen and call the 'sign_in_menu' function to sign out
        clr()
        sign_in_menu()
      else:
        # Clear the console screen and print an error message for an invalid choice
        clr()
        print("Invalid choice, please enter a number between 1 and 5.\n")

    except ValueError:
      # Clear the console screen and print an error message for invalid input (non-integer)
      clr()
      print("Invalid input, please enter a number.\n")


#_________________________________________________________________________________________________________________________________________________________#
# 2.2.1.1. MODIFY LECTURER ACCOUNT

# Define a function named edt_lect
def edt_lect():
  # Access the global variable current_lect
  global current_lect

  # Read existing lecturer accounts from the file
  with open("lecturer_accounts.txt", "r") as file:
      lecturer_accounts = file.read().strip().split("\n\n")

  # Find the account for the currently signed-in lecturer
  lecturer_index = None
  for i, lecturer_account in enumerate(lecturer_accounts):
      stored_username = lecturer_account.split("\n")[8].split(":")[1].strip()
      if current_lect == stored_username:
          lecturer_index = i
          break

  if lecturer_index is not None:
      # Allow the lecturer to edit their username and password
      edited_account = lecturer_accounts[lecturer_index].split("\n")[8].split(":")[1].strip()
      print(f"[EDIT LECTURER ACCOUNT \033[91m{edited_account}\033[0m INFO]\n")
      # Iterate over the lines representing the editable fields (username and password)
      for i in range(8, 10): # Only allow editing of username and password
          field_name, current_value = lecturer_accounts[lecturer_index].split("\n")[i].split(": ")
          # Prompt the user to enter a new value for the current field
          new_value = input(f"\033[91mEnter new {field_name}\033[0m: ").strip()

          # Check if the input is not null or empty
          while not new_value:
              print(f"Error: {field_name} cannot be empty.")
              new_value = input(f"\033[91mEnter new {field_name}\033[0m: ").strip()

          # Update the account details in the list
          lecturer_accounts[lecturer_index] = lecturer_accounts[lecturer_index].replace(f"{field_name}: {current_value}", f"{field_name}: {new_value}")

      # Write the updated accounts back to the file
      with open("lecturer_accounts.txt", "w") as file:
          file.write("\n\n".join(lecturer_accounts) + "\n\n")

      # Update the global variable current_lect with the new username
      current_lect = lecturer_accounts[lecturer_index].split("\n")[8].split(":")[1].strip()

      # Display a success message and wait for user input
      input("\nLecturer account updated successfully.\nPress enter to return...")
      # Clear the console screen
      clr()
  else:
      # Display an error message if the lecturer account is not found and wait for user input
      input("\nLecturer account not found.\nPress enter to return...")
      # Clear the console screen
      clr()

#_________________________________________________________________________________________________________________________________________________________#
# 2.2.1.2. ADD QUESTIONS AND ANSWERS

def add_questions():
    # Read existing subjects and topics from the file
    with open("subjects_and_topics.txt", "r") as file:
        subjects_and_topics = file.read()

    print("[ADD QUESTIONS]\n")

    # Display available subjects and topics
    print(subjects_and_topics)

    # Get the subject name from the user
    user_subject_name = input("Enter the subject name: ")

    # Check if the entered subject name matches any subject name in 'subjects_and_topics.txt'
    if user_subject_name not in subjects_and_topics:
        input(f"\nError: Subject '{user_subject_name}' not found in existing subjects.\nPress enter to return...")
        #input()
        clr()  # Assuming clr() clears the screen
        return

    # Extract the topics for the chosen subject
    topics_start_index = subjects_and_topics.find(f"[SUBJECT {user_subject_name}]")
    if topics_start_index == -1:
        print(f"\nError: Topics not found for subject '{user_subject_name}'.\nPress enter to return...")
        input()
        clr()  # Assuming clr() clears the screen
        return
    topics_end_index = subjects_and_topics.find("\n\n", topics_start_index)
    chosen_subject_topics = subjects_and_topics[topics_start_index:topics_end_index]

    # Get the topic name from the user
    user_topic_name = input("Enter the topic name: ")

    # Check if the entered topic name matches any topic name for the chosen subject
    if user_topic_name not in chosen_subject_topics:
        input(f"\nError: Topic '{user_topic_name}' not found for subject '{user_subject_name}'.\nPress enter to return...")
        #input()
        clr()  # Assuming clr() clears the screen
        return

    # Get information for multiple-choice questions
    num_mcq = 2
    mcq_list = []

    for i in range(num_mcq):
        mcq = input(f"Enter Multiple Choice Question {i + 1}: ")

        # Get options for the multiple-choice question
        options = [input(f"Enter Option {j + 1}: ") for j in range(4)]

        # Get the correct answer
        answer = input("Enter the correct answer (1-4): ")

        mcq_list.append({
            "Question": mcq,
            "Options": options,
            "Answer": answer
        })

    # Get the Essay Question to add (1 question)
    essay_question = input("Enter Essay Question: ")
    essay_answer = input("Enter the answer for the Essay Question: ")

    # Append the questions to the file
    file_path = "questions_and_answers.txt"
    with open(file_path, "a") as file:
        file.write(f"[SUBJECT {user_subject_name} - TOPIC {user_topic_name}]\n")
        for mcq_info in mcq_list:
            file.write(f"  - MCQ: {mcq_info['Question']}\n")
            file.write("\n".join(f"    {chr(ord('A') + j)}. {option}" for j, option in enumerate(mcq_info['Options'])) + "\n")
            file.write(f"    Correct Answer: {chr(ord('A') + int(mcq_info['Answer']) - 1)}\n")
        file.write(f"  - Essay Question: {essay_question}\n")
        file.write(f"    Essay Answer: {essay_answer}\n\n")

    print("Questions added successfully.")
    input("Press enter to return...")
    clr()

#_________________________________________________________________________________________________________________________________________________________#
# 2.2.1.3. MODIFY QUESTIONS AND ANSWERS

def edt_questions():
    # Read existing questions and answers from the file
    with open("questions_and_answers.txt", "r") as file:
        questions_and_answers = file.read()

    print("[EDIT QUESTIONS]\n")

    # Display available questions and answers
    print(questions_and_answers)

    # Get the subject and topic to edit from the user
    user_subject_name = input("Enter the subject name to edit: ")
    user_topic_name = input("Enter the topic name to edit: ")

    # Check if the entered subject and topic match any in the existing questions
    if f"[SUBJECT {user_subject_name} - TOPIC {user_topic_name}]" not in questions_and_answers:
        print(f"\nError: Subject '{user_subject_name}' or Topic '{user_topic_name}' not found in existing questions.\nPress enter to return...")
        input()
        clr()  # Clears the screen
        return

    # Get the updated information for multiple-choice questions
    num_mcq = 2
    mcq_list = []

    for i in range(num_mcq):
        mcq = input(f"Enter updated Multiple Choice Question {i + 1}: ")

        # Get updated options for the multiple-choice question
        options = [input(f"Enter updated Option {j + 1}: ") for j in range(4)]

        # Get the updated correct answer
        answer = input("Enter the updated correct answer (1-4): ")

        mcq_list.append({
            "Question": mcq,
            "Options": options,
            "Answer": answer
        })

    # Get the updated Essay Question
    updated_essay_question = input("Enter updated Essay Question: ")
    updated_essay_answer = input("Enter the updated answer for the Essay Question: ")

    # Identify the section to be modified
    start_index = questions_and_answers.find(f"[SUBJECT {user_subject_name} - TOPIC {user_topic_name}]")
    end_index = questions_and_answers.find("\n\n", start_index)

    # Construct the updated content
    updated_content = f"[SUBJECT {user_subject_name} - TOPIC {user_topic_name}]\n"

    for mcq_info in mcq_list:
        updated_content += f"  - MCQ: {mcq_info['Question']}\n"
        updated_content += "\n".join(f"    {chr(ord('A') + j)}. {option}" for j, option in enumerate(mcq_info['Options'])) + "\n"
        updated_content += f"    Correct Answer: {chr(ord('A') + int(mcq_info['Answer']) - 1)}\n"

    updated_content += f"  - Essay Question: {updated_essay_question}\n"
    updated_content += f"    Essay Answer: {updated_essay_answer}\n\n"

    # Replace the old content with the updated content
    updated_questions_and_answers = questions_and_answers[:start_index] + updated_content + questions_and_answers[end_index:]

    # Write the updated content to the file
    with open("questions_and_answers.txt", "w") as file:
        file.write(updated_questions_and_answers)

    print("Questions updated successfully.")
    input("Press enter to return...")
    clr()

#_________________________________________________________________________________________________________________________________________________________#
# 2.2.1.4. VIEW QUESTIONS AND ANSWERS

def view_questions():
    # Read existing questions and answers from the file
    with open("questions_and_answers.txt", "r") as file:
        questions_and_answers = file.read()

    print("[QUESTIONS LIST]\n")

    # Display available questions and answers
    print(questions_and_answers)

    input("Press enter to return...")
    clr()














#__________________________________________________________________________________________________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________#
# 2.2.1. EXAM UNIT PERSONNEL MENU

# Define a function named examp_menu
def examp_menu():
  # Create an infinite loop for the exam unit personnel menu
  while True:
    # Print a welcome message for the current exam unit personnel
    print(f"Welcome, Exam Unit Personnel {current_examp}!\n")
    # Print the options for the exam unit personnel menu
    print("[EXAM UNIT PERSONNEL MENU]")
    print("1. MODIFY EXAM UNIT PERSONNEL ACCOUNT")
    print("2. CREATE EXAM PAPERS")
    print("3. EDIT EXAM PAPERS")
    print("4. VIEW EXAM PAPERS")
    print("5. SIGN-OUT")

    try:
      # Attempt to get the user's choice as an integer
      choice = int(input("\nEnter your choice (1-5): "))

      # Check the user's choice and perform corresponding actions
      if choice == 1:
        # Clear the console screen and call the 'edt_examp' function to modify exam unit personnel account
        clr()
        edt_examp()
      elif choice == 2:
        # Clear the console screen and call the 'add_expap' function to create exam papers
        clr()
        add_expap()
      elif choice == 3:
        # Clear the console screen and call the 'edt_expap' function to edit exam papers
        clr()
        edt_expap()
      elif choice == 4:
        # Clear the console screen and call the 'view_expap' function to view exam papers
        clr()
        view_expap()
      elif choice == 5:
        # Clear the console screen and call the 'sign_in_menu' function to sign out
        clr()
        sign_in_menu()
      else:
        # Clear the console screen and print an error message for an invalid choice
        clr()
        print("Invalid choice, please enter a number between 1 and 5.\n")

    except ValueError:
      # Clear the console screen and print an error message for invalid input (non-integer)
      clr()
      print("Invalid input, please enter a number.\n")


#_________________________________________________________________________________________________________________________________________________________#
# 2.2.1.1. MODIFY EXAM UNIT PERSONNEL ACCOUNT

# Define a function named edt_examp
def edt_examp():
  # Access the global variable current_examp
  global current_examp

  # Read existing exam unit personnel accounts from the file
  with open("exam_personnel_accounts.txt", "r") as file:
      examp_accounts = file.read().strip().split("\n\n")

  # Find the account for the currently signed-in exam unit personnel
  examp_index = None
  for i, examp_account in enumerate(examp_accounts):
      stored_username = examp_account.split("\n")[0].split(":")[1].strip()
      if current_examp == stored_username:
          examp_index = i
          break

  if examp_index is not None:
      # Allow the exam unit personnel to edit their username and password
      edited_account = examp_accounts[examp_index].split("\n")[0].split(":")[1].strip()
      print(f"[EDIT EXAM UNIT PERSONNEL ACCOUNT \033[91m{edited_account}\033[0m INFO]\n")
      # Iterate over the lines representing the editable fields (username and password)
      for i in range(0, 2): # Only allow editing of username and password
          field_name, current_value = examp_accounts[examp_index].split("\n")[i].split(": ")
          # Prompt the user to enter a new value for the current field
          new_value = input(f"\033[91mEnter new {field_name}\033[0m: ").strip()

          # Check if the input is not null or empty
          while not new_value:
              print(f"Error: {field_name} cannot be empty.")
              new_value = input(f"\033[91mEnter new {field_name}\033[0m: ").strip()

          # Update the account details in the list
          examp_accounts[examp_index] = examp_accounts[examp_index].replace(f"{field_name}: {current_value}", f"{field_name}: {new_value}")

      # Write the updated accounts back to the file
      with open("exam_personnel_accounts.txt", "w") as file:
          file.write("\n\n".join(examp_accounts) + "\n\n")
      # Update the global variable current_examp with the new username
      current_examp = examp_accounts[examp_index].split("\n")[0].split(":")[1].strip()
      # Display a success message and wait for user input
      input("\nExam Unit Personnel account updated successfully.\nPress enter to return...")
      # Clear the console screen
      clr()
  else:
      # Display an error message if the exam unit personnel account is not found and wait for user input
      input("\nExam Unit Personnel account not found.\nPress enter to return...")
      # Clear the console screen
      clr()

#_________________________________________________________________________________________________________________________________________________________#
# 2.2.1.2. MAKE SET EXAM PAPER

# Define a function named add_expap
def add_expap():
    # Print a message indicating the beginning of the process to add experiments or applications
    print("[ADD EXPERIMENTS OR APPLICATIONS]\n")

    # Ask the user to pick Set 1 or Set 2
    set_choice = input("Choose Set (1 or 2): ")

    if set_choice == "1" or set_choice == "2":
        # Implement functionality for Set 1 or Set 2

        # Define file name based on set choice
        expap_file_name = f"expap_{set_choice}.txt"

        # Ask the user to include questions in Section A
        print(f"\n[SET {set_choice} - SECTION A]\n")

        # Read existing questions and answers from the file
        with open("questions_and_answers.txt", "r") as file:
            questions_and_answers = file.read()

        # Get unique multiple-choice questions from questions_and_answers.txt
        unique_mcq_list = []
        for line in questions_and_answers.splitlines():
            if line.startswith("  - MCQ:"):
                question = line.split("  - MCQ: ")[1]
                if question not in unique_mcq_list:
                    unique_mcq_list.append(question)

        # Check if there are enough unique questions for Section A
        if len(unique_mcq_list) < 5:
            print("Error: Insufficient unique multiple-choice questions available.")
            print("Please add more questions in 'questions_and_answers.txt'.")
            input("Press enter to return...")
            clr()
            return

        # Prompt the user to include questions in Section A
        print(f"Include 5 unique multiple-choice questions from 'questions_and_answers.txt' in Section A:")
        section_a_questions = []
        for i in range(5):
            while True:
                question_choice = input(f"Enter Question {i + 1} (choose from existing questions): ")
                if question_choice in unique_mcq_list and question_choice not in section_a_questions:
                    section_a_questions.append(question_choice)
                    break
                else:
                    print("Invalid choice. Please select a unique question from the available options.")

        # Ask the user to include questions in Section B (Essay Questions)
        print(f"\n[SET {set_choice} - SECTION B]\n")

        # Get unique essay questions from questions_and_answers.txt
        unique_essay_list = []
        for line in questions_and_answers.splitlines():
            if line.startswith("  - Essay Question:"):
                question = line.split("  - Essay Question: ")[1]
                if question not in unique_essay_list:
                    unique_essay_list.append(question)

        # Check if there are enough unique questions for Section B
        if len(unique_essay_list) < 3:
            print("Error: Insufficient unique essay questions available.")
            print("Please add more essay questions in 'questions_and_answers.txt'.")
            input("Press enter to return...")
            clr()
            return

        # Prompt the user to include questions in Section B
        print(f"Include 3 unique essay questions from 'questions_and_answers.txt' in Section B:")
        section_b_questions = []
        for i in range(3):
            while True:
                question_choice = input(f"Enter Essay Question {i + 1} (choose from existing questions): ")
                if question_choice in unique_essay_list and question_choice not in section_b_questions:
                    section_b_questions.append(question_choice)
                    break
                else:
                    print("Invalid choice. Please select a unique essay question from the available options.")

        # Save information for Set 1 or Set 2 in respective file
        with open(expap_file_name, "w") as expap_file:
            expap_file.write(f"[SET {set_choice}]\n")
            expap_file.write("Section A Questions:\n")
            for i, question in enumerate(section_a_questions):
                expap_file.write(f"  {i + 1}. {question}\n")

            expap_file.write("\nSection B Essay Questions:\n")
            for i, question in enumerate(section_b_questions):
                expap_file.write(f"  {i + 1}. {question}\n")

        print(f"Information for Set {set_choice} saved in '{expap_file_name}'.")

    else:
        print("Invalid choice. Please enter either '1' or '2'.")

    # Wait for user input before returning and clear the console screen
    input("Press enter to return...")
    clr()  # Assuming clr() clears the screen

#_________________________________________________________________________________________________________________________________________________________#
# 2.2.1.3. EDIT SET 1 and SET 2

# Define a function named edt_expap
def edt_expap():
    # Print a message indicating the beginning of the process to edit experiments or applications
    print("[EDIT EXPERIMENTS OR APPLICATIONS]\n")

    # Ask the user to pick Set 1 or Set 2
    set_choice = input("Choose Set to edit (1 or 2): ")

    # Define file name based on set choice
    expap_file_name = f"expap_{set_choice}.txt"

    try:
        # Read existing information from the file
        with open(expap_file_name, "r") as file:
            expap_content = file.read()

        # Display the current content of the file
        print(expap_content)

        # Get the section to edit (Section A or Section B)
        section_choice = input("Enter the section to edit (A or B): ").upper()

        if section_choice == "A" or section_choice == "B":
            # Get the number of questions to edit
            num_questions = int(input("Enter the number of questions to edit: "))

            # Identify the start and end indices of the section to be modified
            start_index = expap_content.find(f"Section {section_choice} Questions:")
            end_index = expap_content.find("\n\n", start_index)

            # Extract the content of the section to be modified
            section_content = expap_content[start_index:end_index]

            # Prompt the user to enter the updated questions
            updated_questions = []
            for i in range(num_questions):
                updated_question = input(f"Enter updated Question {i + 1}: ")
                updated_questions.append(updated_question)

            # Replace the old content with the updated content
            updated_section_content = f"Section {section_choice} Questions:\n"
            for i, question in enumerate(updated_questions):
                updated_section_content += f"  {i + 1}. {question}\n"

            # Construct the updated content
            updated_expap_content = expap_content.replace(section_content, updated_section_content)

            # Write the updated content to the file
            with open(expap_file_name, "w") as file:
                file.write(updated_expap_content)

            print("Questions updated successfully.")

        else:
            print("Invalid section choice. Please enter 'A' or 'B'.")

    except FileNotFoundError:
        # Display an error message if the file is not found
        print(f"File '{expap_file_name}' not found. Please run 'add_expap' to create the file.")

    # Wait for user input before returning and clear the console screen
    input("Press enter to return...")
    clr()  # Assuming clr() clears the screen

#_________________________________________________________________________________________________________________________________________________________#
# 2.2.1.4. VIEW SET 1 and SET 2

# Define a function named view_expap
def view_expap():
    # Read existing questions and answers from the file for Set 1
    with open("expap_1.txt", "r") as file:
        questions_and_answers_set1 = file.read()

    # Display available Set 1
    print(questions_and_answers_set1)

    # Wait for user input before proceeding to view Set 2
    input("Press enter to view Set 2...")
    # Clear the console screen
    clr()

    # Read existing questions and answers from the file for Set 2
    with open("expap_2.txt", "r") as file:
        questions_and_answers_set2 = file.read()

    # Display available Set 2
    print(questions_and_answers_set2)

    # Wait for user input before returning and clear the console screen
    input("Press enter to return...")
    clr()






# Define a function named main
def main():
    # Call the menu function to start the program
    menu()

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
