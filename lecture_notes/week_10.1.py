# # """
# # given an even number (great than 2), return two prime numbers whoes sum will be equal to the given number.

# # A solution will ALWAYS exist

# # Example:

# # Input: 8 
# # Output: 3 + 5 = 8

# # *note*
# # This is sort of challengin so you can start by just writing a function is_prime(num) which return if a number is prime or not

# # """

# # def is_prime(num):
# #     if num < 2:
# #         return False
# #     for i in range(2, num):
# #         if num % i == 0:
# #             return False
# #     else:
# #         return True


# # def get_prime_pairs()



# # String substrings
# emojis = "🤣😑💀😬🐨🎾🪝🪔💵🍔"

# message = "I love Python🤣😑"

# new_emojis = [char for char in message if char in emojis]
# print(new_emojis)

# letters = ["z","t","c","l"]

# if "l" in letters:
#     print("l is in letters")

# wor1_list = ["l","e","a","d"]
# word2_list = ["d","a","l","e"]

# for letter in wor1_list:
#     if letter in word2_list:
#         pass


# # String Replacing


# sentence = "Our offices are in New York and California."

# sentence = sentence.replace("New York", "NY")
# sentence = sentence.replace("California", "CA")

# print(sentence)


tweets = open("/workspaces/SandBox/tweets.txt")

tweet_lines = tweets.readlines()

total = 0

for line in tweet_lines:
    tweet = line.replace("@VirginAmerica", "")
    total += len(tweet)

avg = total/len(line)

print(avg)