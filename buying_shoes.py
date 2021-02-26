# will not rn because of input() but shows list comp

shoe_sizes_num = input()
shoe_sizes = sorted([int(s) for s in input().split(' ')])

cust_num = int(input())

total = 0

for i in range(cust_num):
    val = [int(s) for s in input().split(' ')]
    
    for x in shoe_sizes:
        if val[0] == x:
            total += val[1]
            shoe_sizes.remove(x)
            break
    
print(total)