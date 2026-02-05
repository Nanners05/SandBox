# functions

"""
1 - Modularity - smaller more manageble chunks
2 - Readability - Helps us read code easier
3 - testing - eaasier to find bugs
4 - organization - organizes code
"""
""" 
1 - definition/name
2 - arguments/parameter
3 - main body of code
4 - return statement
"""

def f_to_c(degrees_f):
    degrees_c = (degrees_f - 32) * (5/9)
    return degrees_c

print(f_to_c(int(input("What is the temperature outside in F? >"))))

def c_to_f(degrees_c):
    degrees_f = degrees_c * (9/5) + 32
    return degrees_f

print(c_to_f(float(input("What is the temperature outside in C? >"))))



# function arguments


# function defualts

print()

age = int(input("How old is child >"))
# weight = int(input("How much does child weigh >"))

def front_seat_check(age, weight=50):
    crit_1 = age >= 12
    crit_2 = age == 11 and weight > 90
    crit_3 = age < 11 and weight > 10

    if crit_1 or crit_2 or crit_3:
        return "The child can sit in the front seat"
    else:
        return "The child cannot sit in the front seat"

print(front_seat_check(age))
