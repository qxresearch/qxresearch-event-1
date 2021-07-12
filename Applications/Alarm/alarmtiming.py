from datetime import datetime
from playsound import playsound
#input the time in HH:MM where HH is  hour and MM is minutes in 12 hour format
alarm_date=input('Enter the date on which you want to set the alarm ').strip()
alarm_time=''.join(input("Enter the time of alarm to be set: HH:MM AM/PM ").split())
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_period=alarm_time[5:7].upper()
print('setting alarm.....')
while True:
    current_time=datetime.now()
    current_hour=current_time.strftime('%I')
    current_minute=current_time.strftime('%M')
    current_period=current_time.strftime('%p')
    current_date=current_time.strftime('%d')
    if current_date==alarm_date and current_period==alarm_period and current_hour==alarm_hour and current_minute==alarm_minute:
        print('*'*10)
        print('| '+'Wake up!'+' |')
        print('*'*10)
        playsound('audio.wav')
        break