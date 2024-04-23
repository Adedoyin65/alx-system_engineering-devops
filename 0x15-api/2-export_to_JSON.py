#!/usr/bin/python3
"""A python script to export data in the JSON format."""
import requests
import json


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

            # Create a dictionary to store the progress data
            progress_data = {
                "employee_name": employee_name,
                "number_of_done_tasks": 0,
                "total_number_of_tasks": len(todos),
                "completed_tasks": []
            }

            # Count the number of completed tasks and store their titles
            for todo in todos:
                if todo['completed']:
                    progress_data['completed_tasks'].append(todo['title'])
                    progress_data['number_of_done_tasks'] += 1

            # Print employee TODO list progress
            a = 'number_of_done_tasks'
            b = 'total_number_of_tasks'
            c = progress_data
            d = employee_name
            print(f"Employee {d} is done with tasks ({c[a]}/{c[b]}):")
            for task in progress_data['completed_tasks']:
                print(f"     {task}")

            # Export progress data to JSON file
            with open(f"{employee_id}.json", "w") as json_file:
                json.dump(progress_data, json_file, indent=4)
            print(f"JSON file {employee_id}.json has been created.")

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
