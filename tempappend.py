import requests
import os
import time
from datetime import datetime

def get_response_content(url):
    try:
        response = requests.get(url)
        content = response.text
        return content
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        return None

# Example usage
url = input("Enter IP: ")
url = f"http://{url}/temp-graph"
interval = input("Enter the time interval (in seconds, default is 60): ")
interval = int(interval) if interval.isdigit() else 60
file_path = "response_log.txt"

time.sleep(2)
with open(file_path, "w") as file:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_time, " Clearing previous data in response_log file")
    file.write("Cleared Previous Data. New log data incoming....\n\n")
time.sleep(2)

print("Script started! Fetching content from {}...".format(url))
time.sleep(2)
counter = 0
while True: 
    content = get_response_content(url)

    if content:
        counter +=1
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = "{} - {}\n".format(current_time, content)

        with open(file_path, "a") as file:
            file.write(log_entry)

        if os.path.isfile(file_path) and os.stat(file_path).st_size > 0:
            print(f"|{counter}| Data appended successfully.")
        else:
            print(f"|{counter}| Error: Failed to append data to file.")
    else:
        print("Error: Failed to retrieve content from the URL.")

    time.sleep(interval)