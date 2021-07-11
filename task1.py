
import os
str = ""

words = []
numbers = []
numbers_raised = []
numbers_max = 0

#Inputting certain string with words and numbers.

str = input("Input your string: ")

#Loop is checking whether string is in digits. Splitting and adding numbers to certain arrays(numbers) or (words). 

for w in str.split():
    if w.isdigit():
        numbers.append(int(w))
    else:
        words.append(w)
str = " ".join(words)

#Output of the string with splitted words.

print("\nOnly words:\n   ", str)

#Loop is capitalising the first and the last letter of every word.

for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:-1] + words[i][-1].upper()
str = " ".join(words)

#Output of the updated string with uppercase letters.

print("\nUpdated string with uppercase letters:\n   ", str)

#Finding the max number with the help of average function max.

#numbers_max = max(numbers)
print("\nJust numbers:", numbers)
print("The max number:", numbers_max)

#Loop is comparing every number in the string to the max. If not adds it to array(numbers_raised), outputs its value, index and idk raised to its index(pidnesennia do stepenia). 

print("Raised to index:")
for i in range(len(numbers)):
    if numbers[i] != numbers_max:
        print("   ", numbers[i], "**", i, "=", numbers[i] ** i)
        numbers_raised.append(numbers[i] ** i)
    else:
        print("   ", numbers[i], "is max(without changes).")

#Output of the numbers raised to the index(kinda pidnesenni do stepenia).

print("\nResult:", numbers_raised)

os.system("pause")
