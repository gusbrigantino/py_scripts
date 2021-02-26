#reverses an int
org_int = -1234567

org_str = str(org_int)

is_neg = False

if (org_str[0] == '-'):
    is_neg = True

if (is_neg):
    org_str = org_str.replace("-", "")

new_str = ""

for x in org_str:
    new_str = x + new_str

if (is_neg):
    new_str = "-" + new_str

int(new_str)
print(new_str)


