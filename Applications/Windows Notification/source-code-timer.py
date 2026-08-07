from win10toast import ToastNotifier
import time

# Create notifier object
toaster = ToastNotifier()

# Take user input
alarm_time = input("Enter time in HH:MM:SS format: ")
title = input("Enter notification title: ")
message = input("Enter notification message: ")

print("Waiting for alarm time...")

while True:
    current_time = time.strftime("%H:%M:%S")

    if current_time == alarm_time:
        toaster.show_toast(title, message, duration=10)
        break