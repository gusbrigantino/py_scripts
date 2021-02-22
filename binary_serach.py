
def main():
    test_input = [2, 23, 5, 7, 99, 101, 7, 3, 5]
    #sort the above list from least to greatest
    sorted_input = BubbleSort(test_input)
    print(sorted_input)

    val = 99
    #search for 99
    result = BinarySearch(val, sorted_input)

    print(result)


def BinarySearch(desired_val, value_list):
    lower = 0
    upper = len(value_list) - 1

    while lower <= upper:
        middle = int((lower + upper ) / 2)
        curr = value_list[middle]

        if curr > desired_val:
            upper = middle -1
        elif curr < desired_val:
            lower = middle + 1
        else:
            return middle


def BubbleSort(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list) - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list


if __name__ == "__main__":
    main()
