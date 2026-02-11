import random

nums = []

for i in range(1,10):
    nums.append(random.randint(1,100))

count = 0
print(nums)
for i in nums:
    if count > 0:
        if nums[count] % 2 == 0 and nums[count - 1] % 2 == 0:
            print(nums[count])
            print(nums[count - 1])
            print("Two evens in a row")
    count += 1