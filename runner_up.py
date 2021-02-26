#reverse sort

scores = [6, 9, 3, 1, 10, 20, 3, 2, 3, 77, 99, 5, 5, 5]

scores = sorted(scores, reverse=True)
    
max_score = scores[0]
runner_up = 0
for x in scores:
    if x < max_score:
        runner_up = x
        break
        
print(runner_up)