test_input = [3, 23, 5, 7, 99, 101, 7, 3, 88, 15, 1, 0, 5]

for i in range(len(test_input)):
    minIndx = i
    for j in range(i + 1, len(test_input)):
        if test_input[minIndx] > test_input[j]:
            minIndx = j
    test_input[i], test_input[minIndx] = test_input[minIndx], test_input[i]

print(test_input)
