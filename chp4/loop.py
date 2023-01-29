
# 4-1

pizzas = ['Pepperoni', 'Hawaian', 'Margarita', 'Napoletana', 'Capricciosa', 'Carnivora', 'Diavola']

for pizza in pizzas:
    print(f'I like {pizza} Pizza')
print('I Love Pizza')

# 4-2

animals = ['Dog', 'Cat', 'Tortle', 'Fish']

for animal in animals:
    print(f'My daughter would love to have a {animal} as pet')
print('We cannot afford having so many pets at home!')

# 4-3

for number in range(1,21):
 print(number)

# 4-4 
print("Separator !")
# for number in range(1,1000001): #condensed output
#     print(number)

# 4-5

ma_millions = list(range(1,1000001))

print(min(ma_millions))
print(max(ma_millions))
print(sum(ma_millions))

# 4-6

odd_numbers = list(range(1,21,2))
for odd in odd_numbers:
    print(odd)

# 4-7

threes = list(range(3,30,3))

for three in threes:
    print(three)

# 4-8

cubes = []
for number in range(1,11):
    cubes.append(number**3)

for cube in cubes:
    print(cube)

# 4-9
print("Separator !")
comprehesive_cube = [number**3 for number in range(1,11)]

for comp_cube in comprehesive_cube:
    print(comp_cube)

# 4-10

print("The Three first items on the list are: ")
print(pizzas[:3])

print("Three Items from the middle are: ")
print(pizzas[int(len(pizzas)/2-1):int(len(pizzas)/2+2)])

print("The last Three Items are: ")
print(pizzas[-3:])

# 4-11

friend_pizzas = pizzas[:]

del friend_pizzas[-2]
friend_pizzas.append("Vegetarian")


print("My favorite pizzas are: ")
for mypizza in pizzas:
    print(mypizza)

print("My friends favorite pizzas are: ")
for friendpizza in friend_pizzas:
    print(friendpizza)

# 4-12

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
for myfood in my_foods:
    print(myfood)

print("My friend's favorite food: ")
for friendfood in friend_foods:
    print(friendfood)

# 4-13

tuple_foods = ('pizza','pasta','lasagna','soup')

for tufood in tuple_foods:
    print(tufood)

# breaking change
# tufood[1] = 'wings'

tuple_foods = ('lentils', 'bread', 'beans')

for tu2food in tuple_foods:
    print(tu2food)