#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

# Send GET request to the URL
response = requests.get('https://alx-intranet.hbtn.io/status')

# Display the body of the response in the specified format
print("- Raw Body:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
