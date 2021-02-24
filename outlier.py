#deletes any outliers in the list based on std dev
import numpy as np

test_input = [1, 2, 5, 15, 20, 23, 23, 23, 23, 24, 24, 26, 26, 27, 28, 29, 50]

new_input = []

average = 0

for x in test_input:
    average += x

average = average / len(test_input)

std_dev = np.std(test_input)

for y in test_input:
    if (y >= average - std_dev and y <= average + std_dev):
        new_input.append(y)

print(average)
print(std_dev)

print("Input: ")
print(test_input)

print("Output: ")
print(new_input)