# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# Jeff Nelson,2020-05-24, Modified code to complete assignment 6
# Jeff Nelson,2020-05-25, Added comments and cleaned up code
# Jeff Nelson,2020-05-31, Added working with binary code
# Jeff Nelson,2020-06-01, Added error handling code
# ---------------------------------------------------------------------------- #

# Import python library
import pickle
import sys

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoList.dat"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions
data_flag = "" # A flag to track if the data has been written to a file


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "rb")
        list_of_rows = pickle.load(file)
        file.close()
        return list_of_rows  # 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Add user inputs into a list of dictionary rows

        :param task: (string) user input:
        :param priority: (string) user input:
        :return: (list) of dictionary rows
        """
        lstTable.append({"Task": task.title(), "Priority": priority.title()})
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Remove user inputs from a list of dictionary rows

        :param task: (string) user input:
        :return: (list) of dictionary rows
        """
        removeItem_flag = 0  # set controller to 0
        for row in lstTable:
            if row['Task'].lower() == task.lower():
                lstTable.remove(row)
                removeItem_flag = 1
                break
        if removeItem_flag == 0:
            print("Task not found in list")
        return list_of_rows  # 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Write data from a a list of dictionary rows into file

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        objFile = open(file_name, "wb")
        pickle.dump(list_of_rows, objFile)
        objFile.close()
        print("Tasks saved to ToDoList.dat")
        return list_of_rows  # 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new task and priority.
        2) Remove an existing task.
        3) Save Data to ToDoList.dat
        4) Reload Data from ToDoList.dat
        5) Exit Program.
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        # print(list_of_rows)
        i = 0
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
            i = 1
        if (i == 0):
            print("No tasks in file. Ready to add tasks!")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gathers the users new task and priority inputs

        :return: string (Tasks)
        :return: string (Priority)
        """
        pass  # TODO: Add Code Here!
        strTask = input("What is the task: ").strip()
        strPriority = input("What is the priority: ").strip()
        return strTask, strPriority  # 'Success'

    @staticmethod
    def input_task_to_remove():
        """ Gathers the users task they would like to remove

        :return: string (Tasks)
        """
        pass  # TODO: Add Code Here!
        task = input("Task to remove: ")
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.dat.
try:
    lstTable = Processor.read_data_from_file(strFileName)  # read file data
except FileNotFoundError as e:
     print("ToDoList.dat not found. Please create!")
     sys.exit()
except Exception as e:
     print("There was a non-specific error!")
     print(e)
     sys.exit()

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    # print(lstTable)
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        # IO.input_press_to_continue(strStatus)
        strTask, strPriority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask, strPriority, lstTable) # should be lstTable not list_of_rows
        data_flag = 1
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here
        # IO.input_press_to_continue(strStatus)
        IO.print_current_Tasks_in_list(lstTable)
        strTask = IO.input_task_to_remove()
        Processor.remove_data_from_list(strTask, lstTable)  # should be lstTable not list_of_rows
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
            # IO.input_press_to_continue(strStatus)
            Processor.write_data_to_file(strFileName, lstTable)
            data_flag = 3
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Add Code Here!
            # IO.input_press_to_continue(strStatus)
            lstTable = Processor.read_data_from_file(strFileName)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        if data_flag == 1:
            strChoice = IO.input_yes_no_choice("You have not saved new data. Are you sure you want Exit? (y/n) -  ")
            if strChoice.lower() == 'y':
                print("Goodbye!")
                break  # and Exit
            else:
                continue  # to shoe the menu
        elif data_flag != 1:
            print("Goodbye!")
            break  # and Exit