from itertools import permutations
arr = ["53", "85"]

is_div_8 = "NO"
ret_list = []

strg = "9927738"

test = list(strg)
newList = list(map(int, test))
print(newList)

my_list = []
for x in arr:
    holder = []
    for c in x:
        holder.append(c)
    my_list.append(holder)

print(my_list)
    
perm_list = []
perm_list.append(permutations(my_list[0]))

for x in list(perm_list):
    for y in list(x):
        print(y[0])
