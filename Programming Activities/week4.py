"""
Programming Activity 1

Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""

year = int(input("In what year were you born? >"))

if 1946 <= year < 1965:
    print("You are a Baby Boomer!!")
elif 1965 <= year < 1981:
    print("You are a Gen X!!")
elif 1981 <= year < 1997:
    print("You are a Millennial!!")
elif year >= 1997:
    print("You are a Zoomer!!")


"""
Programming Activity 2:

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""

age = input("Please input your age >")
current_year = 2026

while True:
    age = int(age)

    if age > 1:
        print(f"you were alive in year: {current_year}")
        age -= 1
        current_year -= 1
        
    else:
        current_year -= 1
        print(f"you were born in year: {current_year}")
        break


"""
Programming Activity 3

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""

for i in range(5,96,5)
    print(i)


"""
Programming Activity 4

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""
x = 5

while x <= 95
    print(x)
    x += 5