'''THE WRONG APPROACH'''

fruits = ("Apple", "Banana")
fruits[1] = "Peaches"
print(fruits)
# Output: Throws an error because tuples are immutable 

'''THE RIGHT APPROACH'''

fruits = ("Apple", "Banana")
# We will convert the tuple into a list and assign it to a new variable

new_fruits = list(fruits)
new_fruits[1] = "Peaches"

# Turning the new list back into a tuple 

fruits = tuple(new_fruits)
print(fruits)

# Output: ("Apple", "Peaches")