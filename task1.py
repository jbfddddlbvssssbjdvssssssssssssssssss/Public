import re

str = input("\nInput the string with numbers and words: ")
word = ''.join([i for i in str if not i.isdigit()])
nums = re.findall(r'\d+', str)
nums = [int(i) for i in nums]

print("\nYour string without numbers:", word)
print("\nYour string without words:", nums)

WithLarge = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in word.split())
print("\nUpdated string with uppercase letters:", WithLarge)

if not nums:
    print("You inputed only words:(")
else:
    nums.remove(max(nums))
    numberIndex = [nums[i]**i for i in range(0,len(nums))]
    print("Array with numbers and indexes:", numberIndex)

print("\n")
