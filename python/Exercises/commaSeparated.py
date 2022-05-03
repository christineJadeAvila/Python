number = input('input comma separated numbers: ')
list = number.split(',')
tuple = tuple(list)

repeating_value = { }
for counts in tuple:
    repeating_value[counts] = tuple.count(counts)

print("List: ", list)
print("Tuple: ", tuple)
print("Repeating Values: ", repeating_value)

color__list = ['red', 'green', 'blue', 'violet']
print(color__list[0], color__list[-1])