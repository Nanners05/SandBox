# split and join

# text = "I really love Aggie Basketball. they can totally beat Villanaova."

# words = text.split(".")

# print(words)

# # .join

# paragraph = ".".join(words)
# print(paragraph)

# person data
# person_data = ["Bob", "Bobson", "56", "Engineer", "Athens"]

# with open("person_data.csv", "w") as file:
#     file.write(", ".join(person_data))

# char test

string = "pAssword123"

print(string.isalnum())

password = input("enger your password. Password must contain 8 letter or numbers but no special characters >")

if password.isalnum() and len(password) >= 8:
    print("Password is acceptable")
else:
    print("Try another password")