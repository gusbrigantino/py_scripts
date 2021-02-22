#gets average word length of a sentence
blurb = "There once was a cat who lived in a vineyard. Her name was Finn, and she loved killing gophers."

#deletes special chars
for sc in ".,?!\";:'":
    blurb = blurb.replace(sc, "")

words = blurb.split(" ")

avg = 0
for x in words:
    avg += len(x)

avg = avg / len(words)

print(avg)