x = "abbaabba"
total = []
for i in range(len(x)):
    #pre = x[0:i]
    suf = x[i:len(x)]

    cnt = 0
    for j in range(len(suf)):
        print(suf[j])
        print(x[j])
        if(suf[j] == x[j]):
            cnt += 1
        else:
            break
    total.append(cnt)

print(total)
