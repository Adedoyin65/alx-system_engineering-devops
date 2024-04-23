#!/usr/bin/python3
"""A python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress"""
import requests


def get_employee_name(employee_id):
    # Construct the URL for the user API endpoint
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        # Send a GET request to the API endpoint
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Convert the response to JSON format
            user_data = response.json()
            # Return the employee name
            return user_data.get('name', 'Unknown')
        else:
            # Print an error message if the request was not successful
            print("Error:", response.status_code)
            return "Unknown"
    except requests.exceptions.RequestException as e:
        # Print an error message if there was a connection error
        print("Connection Error:", e)
        return "Unknown"


def get_todo_progress(employee_id):
    # Construct the URL for the API endpoint
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Send a GET request to the API endpoint
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Convert the response to JSON format
            todos = response.json()

            # Get the employee name
            employee_name = get_employee_name(employee_id)

            # Count the number of completed tasks
            done_tasks = [todo['title'] for todo in todos if todo['completed']]
            number_of_done_tasks = len(done_tasks)

            # Total number of tasks
            total_number_of_tasks = len(todos)

            a = employee_name
            b = number_of_done_tasks
            c = total_number_of_tasks
            # Print employee TODO list progress
            print(f"Employee {a} is done with tasks ({b}/{c}):")

            # Print titles of completed tasks
            for task in done_tasks:
                print(f"     {task}")

        else:
            # Print an error message if the request was not successful
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        # Print an error message if there was a connection error
        print("Connection Error:", e)


if __name__ == "__main__":
    import sys

    # Check if the script is called with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to get the TODO list progress for the employee
    get_todo_progress(employee_id)
