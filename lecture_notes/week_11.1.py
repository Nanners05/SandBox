"""
Using a function rand7() that returns an integer from 1 and 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5

"""
import random

def rand7():
    return random.randint(1,7)

def rand5():
    while True:
        random_num = rand7()
        if random_num not in range(1,6):
            print(random_num)
        else:
            return random_num

print(rand5())