# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   C.Cipolla, 2.21.2024, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
menu_choice: str = ''  # Hold the choice made by the user.
students: list = []  # a table of student data


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    C.Cipolla, 2.21.2024, Created Script
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list) -> list:
        """
        This function reads data from a json file named file_name stored locally
        and returns a list of dictionaries

        ChangeLog: (Who, When, What)
        C.Cipolla, 2.21.2024, Created Script

        :param: file_name
        :param: student_data
        :return: student_data

        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!\n", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list) -> None:
        """
        This function writes data to a json file named file_name stored locally

        ChangeLog: (Who, When, What)
        C.Cipolla, 2.21.2024, Created Script

        :param: file_name
        :param: student_data
        :return: None

        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format\n", e)
        except Exception as e:
            IO.output_error_messages("-- Technical Error Message -- ", e)
        finally:
            if file.closed == False:
                file.close()


class IO:
    """
    A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        C.Cipolla, 2.21.2024, Created Script

    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None) -> None:
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        C.Cipolla, 2.21.2024, Created Script

        :param: message
        :param: exception
        :return: None
        """
        print(f"\n{message}", end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str) -> None:
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        C.Cipolla, 2.21.2024, Created Script

        :param: menu string
        :return: None
        """

        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice() -> str:
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        C.Cipolla, 2.21.2024, Created Script

        :return: string with the users choice
        """
        choice :str = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list) -> None:
        """ This function displays the students' names and courses to the user

        ChangeLog: (Who, When, What)
        C.Cipolla, 2.21.2024, Created Script

        :return: None
        """

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list) -> str:
        """ This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        C.Cipolla, 2.21.2024, Created Script

        :return: str
        """

        while True:
            try:
                # Input the data
                student_first_name = input("What is the student's first name? ")
                if not student_first_name.isalpha():
                    raise ValueError("The first name should only contain letters.\nPlease try again")

                student_last_name = input("What is the student's last name? ")
                if not student_last_name.isalpha():
                    raise ValueError("The last name should only contain letters.\nPlease try again")

                course_name = input("Please enter the name of the course: ")
                student = {"FirstName": student_first_name,
                                "LastName": student_last_name,
                                "CourseName": course_name}
                student_data.append(student)
            except ValueError as e:
                IO.output_error_messages(message = e)
            except Exception as e:
                IO.output_error_messages("There was a non-specific error!", e)
            else:
                return student_data
                break


#  End of function definitions


# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break  # out of the while loop