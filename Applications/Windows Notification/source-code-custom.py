import win10toast
toaster = win10toast.ToastNotifier()
title = input("Enter notification title: ")
message = input("Enter notification message: ")

toaster.show_toast(title, message, duration=10)