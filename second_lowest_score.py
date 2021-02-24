if __name__ == '__main__':
    names = ["Mia", "Gus", "Ted", "Bill", "Anthony"]
    scores = [99, 2, 24, 97, 24]
        
    desired_indxs = []
    
    for i in range(len(scores)):
        midIndex = i
        for j in range(i + 1, len(scores)):
            if scores[midIndex] > scores[j]:
                midIndex = j
        scores[i], scores[midIndex] = scores[midIndex], scores[i]
        names[i], names[midIndex] = names[midIndex], names[i]
    
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
    
        
    
