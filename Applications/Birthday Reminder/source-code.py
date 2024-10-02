import datetime
import smtplib
from email.mime.text import MIMEText
from plyer import notification

# Log of birthdays
bday_log = [
   ('Ayushi', ('1999', '10', '19')),
   ('Yash', ('1999', '04', '21')),
]

# Current date processing
current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')

# Function to send email notifications
def send_email_notification(name, age):
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_email_password"

    subject = f"Reminder: It's {name}'s Birthday!"
    body = f"It's {name}'s {age}th birthday today!"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Function to show desktop notification
def send_desktop_notification(name, age):
    notification.notify(
        title="Birthday Reminder",
        message=f"It's {name}'s {age}th Birthday today!",
        app_name='Birthday Reminder',
        timeout=10
    )

# Add birthday functionality
add = input('To add birthday type y:').strip().lower()

if add == 'y':
   new = input('Add birthday in format yyyy-mm-dd:')
   name = input('Whose bday?')
   date = new.split('-')
   bday_log.append((name, tuple(date)))

# Checking for birthdays today
for birthday in bday_log:
   if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
       age = int(current_date_lst[0]) - int(birthday[1][0])
       ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <= 13 else age % 14, 'th')
       
       print(f" It's {birthday[0]}'s {age}{ordinal_suffix} Birthday")

       # Send email notification
       send_email_notification(birthday[0], age)

       # Show desktop notification
       send_desktop_notification(birthday[0], age)
