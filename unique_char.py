#using a dict as a counter

#finds unique chars in string
test_input = "aaaaaaaaaxssssaaaa"

tracker = {}

for x in test_input:
    if x not in tracker:
        tracker[x] = 1
    else:
        tracker[x] += 1

unique_char = ''
var = []
for y in tracker:
    if tracker[y] == 1:
        var.append(y)

if not var:
    var = "N/A"

index = []
for v in var:
    try:
        index.append(test_input.index(v))
    except:
        pass

if not index:
    index = -1

print(var)
print(index)