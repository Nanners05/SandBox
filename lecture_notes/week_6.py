"""
Given a lost of numbers, and a number 'k', return whether any two numbers from the list add up to 'k'

"""

numbers = [10, 15, 3, 7]
k = 17

def target_num(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                print("Found", target, "in number list")
                break

target_num(numbers, k)



# basics

colors = ["Purple", "Green", "Aggie Blue"]
print("Colors:", colors)
colors.append("Fighting White")
print("colors:", colors)

colors.pop(1)
print("colors:", colors)

colors.insert(0, "Pink")
print("colors:", colors)

# search/slice and sorting lists

colors[3]

for i in colors:
    print("colors:", i)

# figure our if two words are anagrams

def is_anagram(word1, word2):
    word_1_list = []
    word_2_list = []
    if word1 == len(word2):
        for i in word1:
            word_1_list.append(i)
        for i in word2:
            word_2_list.append(i)
        return sorted(word_1_list) == sorted(word_2_list)
    return False

if is_anagram("silent", "listen"):
    print("They are anagrams!")
else:
    print("NOPE")


