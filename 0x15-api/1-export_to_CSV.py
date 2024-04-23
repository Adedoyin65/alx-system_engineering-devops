#!/usr/bin/python3
"""A python script to export data in the CSV format."""
import requests
import csv


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

            # Open a CSV file with the employee ID as the filename
            with open(f"{employee_id}.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                a = "TASK_COMPLETED_STATUS"
                # Write the header row
                writer.writerow(["USER_ID", "USERNAME", a, "TASK_TITLE"])

                # Write each task owned by the employee to the CSV file
                b = employee_name
                c = 'completed'
                d = 'title'
                for todo in todos:
                    writer.writerow([todo['userId'], b, todo[c], todo[d]])

            print(f"CSV file {employee_id}.csv has been created successfully.")

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

    # Call the function to get export to CSV
    get_todo_progress(employee_id)
