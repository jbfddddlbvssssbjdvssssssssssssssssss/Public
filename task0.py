



import random
a_list = []
for i in range(1,30):
    a_list.append(random.randint(-100,100))
    
max_value = max(a_list)

max_index = a_list.index(max_value)
print(a_list)
print(max(a_list))

print(max_index)

for i in range(len(a_list)-1):
    print(a_list[i],a_list[i+1]) if a_list[i]<0 and a_list[i+1]<0 else None

