# 5-1

car = 'Kia'
print("Is Car equal to Kia?, I predict True")
print(car == 'Kia')

print("is Car equal to Chevrolet?, I predict False")
print(car == 'Chevrolet')

print("is Car equal to kia?, I prefict False")
print(car == 'kia')

print("wait, but car brands do not matter how are they written, right?")
print(f"Sorry then, {car.lower() == 'kia'}")

print("Let's try to play again, think of another car brand")
car = 'Subaru'

print('is Car not equal to Kia? I predict True')
print(car != 'Kia')

print("is Car equal to Ford? I predict False")
print(car == 'Ford')

print("wait, do we care about format? again?")
print(f"We do but still is, {car == 'Ford'}")

print("Does it start with S? I predict True")
print(car[0] == 'S')

print("Right so is it Samurai?")
print(f"huh, that does not seem like a brand to me? {car == 'Samurai'}")

print("Hahahaha I was just kidding, Subaru?? I predict True")
print(f"Finally, you have got it, predict {car == 'Subaru'}")

# 5-2
fruit = 'Apple'
print(f"is Fruit different than Mandarin ? {fruit != 'Mandarin'}")
print(f'is Fruit an Apple? {fruit == "Apple"}')

print(f'is an Apple different than an apple? { fruit.lower() == "apple"}, { fruit.lower() != "Apple"}')

number_people = 57

print(f'Is the number of people greater than 5 ? { number_people > 5 }')
print(f'Is the number of people less than 5? { number_people < 5 }')
print(f'is the number of people less than 100 but greater than 20? { number_people < 100 and number_people > 20 }')
print(f'is the number of people lower or equals than 60 or greater than 70 ? { number_people <= 60 or number_people > 70}' )
print(f'is the number of people equal to 50? { number_people == 50 }')
print(f'is the number 57 ? { number_people == 57 }')

sports_liked = ['Skateboarding', 'Basketball', 'Soccer']

print(f'is one of your favorite sports Baseball? { "Baseball" in sports_liked }')
print(f'I guess then you do not like Basketball? { "Basketball" not in sports_liked }')