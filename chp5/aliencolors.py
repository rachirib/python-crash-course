# 5-3
alien_color = 'red'

if alien_color == 'green':
    print('There you go 5 points')

alien_color = 'green'
if alien_color == 'green':
    print('Ok 5 points...')

# 5-4

alien_color = 'yellow'

if alien_color == 'green':
    print('You\' got 5 points')
else:
    print('You\'ve got 10 points')

alien_color = 'green'

if alien_color == 'green':
    print('5 points for this')
else:
    print('10 points for that')

# 5-5

alien_color = 'red'

if alien_color == 'green':
    print('5 points for you my friend')
elif alien_color == 'yellow':
    print('10 points for that mellow')
elif alien_color == 'red':
    print('15 good one mate.')

alien_color = 'green'

if alien_color == 'green':
    print('5 points hey')
elif alien_color == 'yellow':
    print('10 points for that')
elif alien_color == 'red':
    print('Red as a pepper 15 points')

alien_color = 'yellow'

if alien_color == 'green':
    print('5 points for that green')
elif alien_color == 'yellow':
    print('10 points for that egg')
elif alien_color == 'red':
    print('15 points for that chili')

# 5-6

age = 65

if age < 2:
    print('You are a baby')
elif age >= 2 and age < 4:
    print('You are a toddler')
elif age >= 4 and age < 13:
    print('You are a kid')
elif age >= 13 and age < 20:
    print('You are a teenager')
elif age >= 20 and age < 65:
    print('You are an adult')
elif age >= 65:
    print('You are an elder')

# 5-7

favourity_fruits = ['Apple','Kiwi','Pineapple']

if 'Dragonfruit' in favourity_fruits:
    print('You really like Bananas!')
if 'Passionfruit' in favourity_fruits:
    print('You really like Bananas!')
if 'Kiwi' in favourity_fruits:
    print('You really like Bananas! Men')


# 5-8

users = ['negadyno','blackwillow69','numbertwo','admin','theguywiththevan']
# users = [] 5-9
if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, would you like an status report?')
        else:
            print(f"Hello {user}, Thank you for logging in again.")
else:
    print("We need some users!")


# 5-10
current_users = ['negadyno','blackwillow69','numbertwo','admin','theguywiththevan']
new_users = ['positivenenergy','myfriendismissing','blackWILLOW69','negaDyno']

lower_entries = [ user.lower() for user in new_users]

for new_user in lower_entries:
    if new_user in current_users:
        print(f'Sorry but {new_user} as already being taken')
    else:
        print(f'User {new_user} has been created successfully')


# 5-11

ordinal_numbers = ['1','2','3','4','5','6','7','8','9']

for number in ordinal_numbers:
    if number == '1':
        print(f'{number}st')
    elif number == '2':
        print(f'{number}nd')
    elif number == '3':
        print(f'{number}rd')
    else:
        print(f'{number}th')