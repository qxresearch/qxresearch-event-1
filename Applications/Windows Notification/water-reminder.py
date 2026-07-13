from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

while True:
    toaster.show_toast(
        "Hydration Reminder 💧",
        "Time to drink water!",
        duration=10
    )

    time.sleep(3600)