#two dict sort based on one's values, second lowest value, sorted call

if __name__ == '__main__':
    names = ["Mia", "Gus", "Ted", "Bill", "Anthony"]
    scores = [99, 2, 24, 97, 24]
        
    desired_indxs = []
    
    for i in range(len(scores)):
        minIndex = i
        for j in range(i + 1, len(scores)):
            if scores[minIndex] > scores[j]:
                minIndex = j
        scores[i], scores[minIndex] = scores[minIndex], scores[i]
        names[i], names[minIndex] = names[minIndex], names[i]
    
    second = 0
    for i in range(len(scores)):
        if scores[i] > scores[0]:
            second = i
            break
    
    for i in range(len(scores)):
        if scores[i] == scores[second]:
            desired_indxs.append(i)
        
    desired_names = []
    for x in desired_indxs:
        desired_names.append(names[x])
    
    output = sorted(desired_names)
    
    for name in output:
        print(name)
    
        
    
