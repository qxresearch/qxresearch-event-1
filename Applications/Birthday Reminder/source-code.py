import datetime

def calculate_age(birthdate, current_date):
    birth_year, birth_month, birth_day = map(int, birthdate)
    current_year, current_month, current_day = map(int, current_date)

    age = current_year - birth_year
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1

    ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <= 13 else age % 14, 'th')
    
    return age, ordinal_suffix
   
current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')
bday_log = [
   ('Ayushi', ('1999', '10', '19')),
   ('Yash', ('1999', '04', '21')),
]
add = input('To add birthday type y:').strip().lower()

if add[:1] == 'y':
   new = input('Add birthday in format yyyy-mm-dd:')
   # print(new_lst)
   name = input('Whose bday?')
   date = new.split( '-' )


   bday_log.append((name, tuple(date)))

for birthday in bday_log:
   # current_dat[1] == birthday[1][1] this will check if current month is same as birth month  and current date is same as
   # birth date as per preadded log


   if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
       age = int(current_date_lst[0]) - int(birthday[1][0])
       ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <= 13 else age % 14, 'th')
       print(f" It's {birthday[0]}'s {age}{ordinal_suffix} Birthday")

