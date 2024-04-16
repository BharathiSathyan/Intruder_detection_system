import cv2
import numpy as np
from pushbullet import PushBullet
import win32com.client as wincl
import time
import os
import socket
import json
import datetime
import geocoder





#takes intruder pic
def intruder_pic():
    cam = cv2.VideoCapture(0)
    s, im = cam.read()
    cv2.imwrite("Intruder.bmp", im)

# Voice message
def suspected_message(str):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(str)

# Your PushBullet API key
api_key = "o.1qAb1tdd8GYbLEnVdcBUyCpefqaDsNNm"
pb = PushBullet(api_key)
pushMsg = pb.push_note("PYTHON: ", "Found Internet Connectivity, is this you? ['Yes'/'No'] ")

# Pushes captured image to Mobile
def Image_send():
    with open("Intruder.bmp", "rb") as pic:
        file_data = pb.upload_file(pic, "Intruder.bmp")
    push = pb.push_file(**file_data)

# Log off PC if Intruder Suspected
def logOff():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# Function to save IP address to a file
def save_ip_address(data):
    with open('intruder_ip_addresses.json', 'a') as file:
        json.dump(data, file)
        file.write('\n')


# Function to record the IP address of the current system
def record_ip_address():
    try:
        # Get the hostname of the system
        hostname = socket.gethostname()
        # Get the IP address corresponding to the hostname
        ip_address = socket.gethostbyname(hostname)
        # Get current time and date
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Get current location (latitude, longitude)
        g = geocoder.ip('me')
        location = g.latlng if g.latlng else None
        place = g.city if g.city else "Unknown"
        # Save the IP address data to a file
        data = {
            'time': current_time,
            'place': place,
            'ip_address': ip_address,
            'hostname': hostname
        }
        save_ip_address(data)
        print(f"Intruder Data recorded: {data}")
    except Exception as e:
        print(f"An error occurred while recording IP address: {e}")




def read_ip_addresses():
    try:
        with open('intruder_ip_addresses.json', 'r') as file:
            for line in file:
                data = json.loads(line)
                print("Time:", data['time'])
                print("Place:", data['place'])
                print("IP Address:", data['ip_address'])
                print("Hostname:", data['hostname'])
                print()
    except FileNotFoundError:
        print("File 'intruder_ip_addresses.json' not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")




# Controller
def Control(password):
    og_pass = "123hi"  # Original password
    if(password != og_pass):
        suspected_message("Intruder Suspected")
        intruder_pic()
        Image_send()
        # Record IP address of the intruder
        record_ip_address()
        time.sleep(15)
        val = pb.get_pushes()
        if val:
            action = val[0].get('body', None)  # Check if 'body' key exists
            if action:
                print(action)
                if action.lower() == 'no':
                    suspected_message("Logging Off")
                    logOff()
                elif action.lower() == 'yes':
                    suspected_message("Safe, No Intruder")
                    print("Safe, No Intruder")
            else:
                print("No 'body' key found in push data.")
        else:
            print("No pushes available.")
    else:
        suspected_message("Safe, No Intruder")
        print("Safe, No Intruder")

def main():
    user = "Bharathi"
    password = input(f"Enter Password for account @{user} : ")
    Control(password)


# Entry point of the script
if __name__ == "__main__":
    main()
read_ip_addresses()