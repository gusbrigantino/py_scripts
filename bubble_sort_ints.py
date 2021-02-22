test_input = [2, 23, 5, 7, 99, 101, 7, 3, 88, 15, 1, 0, 5]
print(test_input)

#sorts above list
for i in range(len(test_input)):
    for j in range(len(test_input) - i - 1):
        if test_input[j] > test_input[j + 1]:
            test_input[j], test_input[j + 1] = test_input[j + 1], test_input[j]

print(test_input)
