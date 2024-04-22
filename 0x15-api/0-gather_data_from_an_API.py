#!/usr/bin/python3
# A python script that, using this REST API, for a given employee
# ID, returns information about his/her TODO list progress.
import json
import urllib.request


def get_user_name(user_id):
    # Construct the URL for the user API endpoint
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        # Send a GET request to the API endpoint
        with urllib.request.urlopen(url) as response:
            # Read the response and decode it from bytes to a string
            data = response.read().decode("utf-8")
            # Convert the response string to a JSON object
            user_data = json.loads(data)
            # Return the username
            return user_data['username']

    except urllib.error.HTTPError as e:
        # Print an error message if the HTTP request fails
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        # Print an error message if there was a connection error
        print(f"Connection Error: {e.reason}")
    return "Unknown"


def get_todo_progress(employee_id):
    # Construct the URL for the API endpoint
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Send a GET request to the API endpoint
        with urllib.request.urlopen(url) as response:
            # Read the response and decode it from bytes to a string
            data = response.read().decode("utf-8")
            # Convert the response string to a JSON object
            todos = json.loads(data)

            # Get the employee name
            employee_name = get_user_name(employee_id)

            # Count the number of completed tasks
            done_tasks = [todo['title'] for todo in todos if todo['completed']]
            number_of_done_tasks = len(done_tasks)

            # Total number of tasks
            total_number_of_tasks = len(todos)

            # Print employee TODO list progress
            a = employee_name
            b = number_of_done_tasks
            c = total_number_of_tasks
            print(f"Employee {a} is done with tasks ({b}/{c}):")
            # Print titles of completed tasks
            for task in done_tasks:
                print(f"\t{task}")

    except urllib.error.HTTPError as e:
        # Print an error message if the HTTP request fails
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        # Print an error message if there was a connection error
        print(f"Connection Error: {e.reason}")


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
