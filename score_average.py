#dictionary example and string format example

n = 3

student_marks = {"Logan": [87, 34, 55], "Jack": [77, 88, 99], "Stef": [10, 50, 40]}

query_name = "Stef"

desired_scores = student_marks[query_name]

avg = 0

for x in desired_scores:
    avg += x

avg = avg / len(desired_scores)

result = "{:.2f}".format(avg)

print(result)