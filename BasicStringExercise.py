#Problem 1:
stringy = "Everything is an Object in Python!!"

print(stringy)
print(stringy.upper())
print(stringy.lower())
print(stringy.capitalize())

first_name = "Marlie"
last_name = "Martinez"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

phrase = "Reindeer games"
print(phrase.rstrip())
print(phrase.lstrip())
print(phrase.strip())

#Problem 2: 
Famous = "Valerie"
Quote = "Patience, young grasshopper"
print(f'{Famous} once said, "{Quote}."')
print("{} once, said '{}.'".format(Famous, Quote))

course = "Per Scholas"
print(course[1])
print(course[3])
print(course[-5])

string1 = "slicing strings is easy!"
print(string1[:3])
print(string1[1: 6: 2])
print(string1[-1: -8: -2])
print(string1[: : -1])

#Problem 3: 
# Reverse the entire string
# Get the last charachter of the string
# Get every other chrachter in the string
# Check the length of the string
# Get the 4th charachter in the string
# Get the 4th charachter through the 9th charachter in the string
# Get the 7th through last charachter in the string

marlies_string = "Hi my name is Marlie!"
print(marlies_string[: : -1])
print(marlies_string[ : : 2])
print(len(marlies_string))
print(marlies_string[3])
print(marlies_string[3 : 10])
print(marlies_string[6 : -1])