# Ricardo Chiriboga - List introduction

# 3-1

my_friends = ['Juan David Osorio', 'Wilson Reyes', 'Juan Manuel Caicedo']

print(my_friends[0])
print(my_friends[1])
print(my_friends[2])


# 3-2

print(f'{my_friends[0]} like to pick their nose')
print(f'{my_friends[1]} like to pick their nose')
print(f'{my_friends[2]} like to pick their nose')


# 3-3

favourity_transport = ['its believe that public transportation helps the environment',
 'public transport is a treat on developing countries', 
 'it is easy to follow up trail station guidelines']

print(favourity_transport[0])
print(favourity_transport[1])
print(favourity_transport[2])

# 3-4

guest_lists = ['Gandhi', 'Albert Einstein', 'Papa Juan Pablo II', 'Isabelle Chiriboga Rico']

print(f'Hi, {guest_lists[0]} your are invited to dinner!')
print(f'Hi, {guest_lists[1]} your are invited to dinner!')
print(f'Hi, {guest_lists[2]} your are invited to dinner!')
print(f'Hi, {guest_lists[3]} your are invited to dinner!')

# 3-5

print(f'{guest_lists[1]} cannot make it to the dinner :( ')

guest_lists[1] = "Wifey"

print(f'Hi, {guest_lists[0]} your are invited to dinner!')
print(f'Hi, {guest_lists[1]} your are invited to dinner!')
print(f'Hi, {guest_lists[2]} your are invited to dinner!')
print(f'Hi, {guest_lists[3]} your are invited to dinner!')

# 3-6

print('it seems that there is a bigger table!')

guest_lists.insert(0,'Mama')
guest_lists.insert(2,'Papa')
guest_lists.append("Luchini")

print(f'Hi, {guest_lists[0]} your are invited to dinner!')
print(f'Hi, {guest_lists[1]} your are invited to dinner!')
print(f'Hi, {guest_lists[2]} your are invited to dinner!')
print(f'Hi, {guest_lists[3]} your are invited to dinner!')
print(f'Hi, {guest_lists[4]} your are invited to dinner!')
print(f'Hi, {guest_lists[5]} your are invited to dinner!')
print(f'Hi, {guest_lists[6]} your are invited to dinner!')

# 3-7

print("I'm so sorry but we only got one table we will have to make arrangements for next time")

print(f'{guest_lists.pop(0)} sorry but we will go out next time')
print(f'{guest_lists.pop(0)} sorry but we will go out next time')
print(f'{guest_lists.pop(0)} sorry but we will go out next time')
print(f'{guest_lists.pop(1)} sorry but we will go out next time')
print(f'{guest_lists.pop(2)} sorry but we will go out next time')

print(f'{guest_lists[0]} you are still invited')
print(f'{guest_lists[1]} you are still invited')

del guest_lists[0]
del guest_lists[0]

print(f'{guest_lists} this should be clean')

# 3-8

places_list = ['Silicon Valley', 'Hobby Town', 'London', 'Venecia', 'Berlin']

print(places_list)
print(sorted(places_list))
print(places_list)
print(sorted(places_list, reverse=True))
print(places_list)
places_list.reverse()
print(places_list)
places_list.reverse()
print(places_list)
places_list.sort()
print(places_list)
places_list.sort(reverse=True)
print(places_list)

# 3-9

print(f'Number of Guest Invited: {len(guest_lists)}')

# 3-10

languages = ["Spanish", "English", "French", "Italian", "Greek", "Arabic"]
print(languages)

languages.insert(2, "Filipino")
languages.append("Chinese")
print(languages)

print(sorted(languages))
print(sorted(languages, reverse=True))
languages.sort()
print(languages)
languages.reverse()
print(languages)

print(f'You are poped: {languages.pop(3)}')
del languages[3]

languages.sort(reverse=True)
print(languages)
