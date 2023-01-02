values = (input('Input a list of student heights: ')).split()
scores = []

for i in values:
    scores.append(int(i))

# to get the highest score
high_score = 0
for i in scores:
    if i > high_score:
        high_score = i

print(f'The highest score in the class is : {high_score}')
