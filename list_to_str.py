#string to list then back to string

test_input = "aaaaaaaxbbbbbbb"
char = 'b'
index = 7

holder = list(test_input)

holder[index] = char

output = ''.join(holder)

print(output)