kor_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]

scores = [kor_score, math_score, eng_score]

print(scores)

for student in range(5):
    sum = 0
    for i in range(3):
        sum += scores[i][student]

avg = sum / 3

print(avg)