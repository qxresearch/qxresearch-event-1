import datetime

def get_current_date():
    return datetime.date.today().strftime('%Y-%m-%d')

def get_birthday_log():
    return [
        ('Ayushi', ('1999', '10', '19')),
        ('Yash', ('1999', '04', '21')),
    ]

def add_birthday(bday_log):
    new_birthday = input('Add birthday in format yyyy-mm-dd:')
    name = input('Whose birthday?')
    date = new_birthday.split('-')
    bday_log.append((name, tuple(date)))
    return bday_log

def display_birthdays_today(bday_log, current_date):
    current_date_lst = current_date.split('-')
    for birthday in bday_log:
        if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
            age = int(current_date_lst[0]) - int(birthday[1][0])
            ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <= 13 else age % 14, 'th')
            print(f"It's {birthday[0]}'s {age}{ordinal_suffix} Birthday")

def main():
    current_date = get_current_date()
    bday_log = get_birthday_log()
    add = input('To add birthday type y:').strip().lower()

    if add.startswith('y'):
        bday_log = add_birthday(bday_log)

    display_birthdays_today(bday_log, current_date)

if __name__ == "__main__":
    main()


