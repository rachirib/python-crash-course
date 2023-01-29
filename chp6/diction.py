


know_you = {
    'first_name' : 'Wolfgang',
    'middle_name' : 'Amadeus',
    'last_name' : 'Mozart',
    'phone_number' : '77693907',
    'age' : '23456789',
    'city' : 'Berlin'
}

print(know_you.get('first_name'))
print(know_you.get('middle_name'))
print(know_you.get('last_name'))
print(know_you.get('phone_number'))
print(know_you.get('age'))
print(know_you.get('city'))


favourite_numbers = { 
    'Juan Peroline': 5,
    'Jessica Strudness' : 10, 
    'Myla Maldiva' : 4,
    'Pedro Pelicula' : 8,
    'Michael Sativa' : 2
}
print(f'Juan Peroline favourite number is: {favourite_numbers.get("Juan Peroline")}')
print(f'Jessica Strudness favourite number is: {favourite_numbers.get("Jessica Strudness")}')
print(f'Myla Maldiva favourite number is: {favourite_numbers.get("Myla Maldiva")}')
print(f'Pedro Pelicula favourite number is: {favourite_numbers.get("Pedro Pelicula")}')
print(f'Michael Sativa favourite number is: {favourite_numbers.get("Michael Sativa")}')

glossary = {
    'loops': 'Used to pass through data structures',
    'dictionaries': 'Also known as hash maps, allow to organise information usin key and value structure',
    'identation': 'Python indent code so conditional and scope is maintained',
    'microprofile' : 'Java framework for running microservices with bare minimun infrastructure specs',
    'resteasy': 'Java framework to build rest endpoints'
}

print(f'loops:\n\t{glossary.get("loops")}' )
print(f'dictionaries:\n\t{glossary.get("dictionaries")}')
print(f'identation:\n\t{glossary.get("identation")}')
print(f'microprofile:\n\t{glossary.get("microprofile")}')
print(f'resteasy:\n\t{glossary.get("resteasy")}')