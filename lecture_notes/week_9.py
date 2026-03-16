"""
Write a function that implements division with two positive integers without using the division, multiplication or modulouls operator.
Return the quotient as an integers, and ignore the remainder

"""
# def division(divisor, dividend):
#     quotient = 0
#     sum = 0
#     while divisor >= dividend:
#         sum += dividend
#         quotient += 1
#     return quotient

# print(division(25,5))

#List comprehension

"""
newList = [expression for idem in iterable if condition]

"""

# nums = [1,2,3,4,5,6,7,8,9,10]

# evenNums = [num for num in nums if num % 2 == 0]

# print(evenNums)


# text = "teach a man to fish"
# chars = [char for char in text if char != " "]
# print(chars)

# words = ["tacocat", "dog", "racecar", "swag", "civic"]

# pals = [word for word in words if word[::-1] == word]
# print(pals)

# string1 = "hello"
# string2 = "world"

# age = 20
# name = "Steve"
# sentence = "Hi, my name is " + name + " and I am "  + str(age) + " years old."
# print(sentence)

# fruit = "pineapple"
# fruit += " is the best"
# print(fruit)

# name = "       Big Blue         "
# print(name)
# name.rstrip()
# name.lstrip()
# name.strip()

# print(name.strip())

# name.capitalize()
# name.upper()
# name.lower()
# name.title()
# name.isupper()
# name.islower()
# name.istitle()
# name.isdigit()

paragraph = "Today is wendesday and I sometimes don't like those days because I want it to be the end of the week and it's only the middle. Also, I feel like Wednesday is literally mid."
words = paragraph.split(" ")
words2 = paragraph.rsplit()

print(words2)