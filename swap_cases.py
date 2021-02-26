test_input = "String TOO test THE uppER and LOWER CasES"

output = ""

for x in test_input:
    if x == ' ':
        output += ' '
    elif x.islower():
        output += x.upper()
    else:
        output += x.lower()


print(output)