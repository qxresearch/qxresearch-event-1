import datetime
import time
from rich.console import Console                                # Rich module

rc = Console()                                                  # Rich Console for adding more indulging output

current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')
bday_log = [
   ('Ayushi', ('1999', '10', '19')),
   ('Yash', ('1999', '04', '21')),
]
add = input('To add new entry into birthday logs (y/n):').strip().lower()

if add[:1] == 'y':
    new = str(input('Add birthday in format yyyy-mm-dd:'))      # Convert date value to string for convenience in logging
    # print(new_lst)
    name = str(input('Whose bday?'))                            # Convert name to string for convenience in logging
    date = new.split( '-' )

    bday_log.append((name, tuple(date)))

elif add[:1] == 'n':
    rc.print("Checking the logs..", style="cyan")
    time.sleep(1)
    for birthday in bday_log:
        # current_dat[1] == birthday[1][1] this will check if current month is same as birth month  and current date is same as
        # birth date as per preadded log


        if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
            age = int(current_date_lst[0]) - int(birthday[1][0])
            ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <= 13 else age % 14, 'th')
            rc.print(f"It's {birthday[0]}'s {age}{ordinal_suffix} Birthday :partying_face::birthday_cake:", style="green")

        else:
            rc.print(f"{birthday[0]}'s birthday is not today :clock5:", style="yellow")

else:
    rc.print("Please provide a valid input", style="red")
