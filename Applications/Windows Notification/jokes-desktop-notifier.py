import pyjokes
import time
from win10toast import ToastNotifier 

while 1:
    notify = ToastNotifier()
    notify.show_toast("Time to laugh!", pyjokes.get_joke(), duration = 20)
    time.sleep(1800)
