"""
print('Welcome to the Love Calculator!')
lover_one = input('What is your name?\n').replace(" ", '')
print(lover_one)
lover_two = input('What is their name?\n').replace(" ", '')
print(lover_two)
check_one = 'truelove'
checker_one = 0
checker_two = 0

for i in lover_one.lower():
    for j in check_one.lower():
        checker_one += i.count(j)

for i in lover_two.lower():
    for j in check_one.lower():
        checker_two += i.count(j)

love_score = int(str(checker_one) + str(checker_two))
if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}%, you go together like coke and mentos.')
elif (love_score >= 40) or (love_score <= 50):
    print(f'Your score is {love_score}%, you are alright together.')
else:
    print(f'Your score is {love_score}%.')

"""

print('Welcome to the Love Calculator!')
lover_one = input('What is your name?\n').replace(" ", '').lower()
lover_two = input('What is their name?\n').replace(" ", '').lower()
check_one = 'truelove'
checker_one = sum(lover_one.count(ch) for ch in check_one)
checker_two = sum(lover_two.count(ch) for ch in check_one)

love_score = int(str(checker_one) + str(checker_two))
if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}%, you go together like coke and mentos.')
elif (love_score >= 40) or (love_score <= 50):
    print(f'Your score is {love_score}%, you are alright together.')
else:
    print(f'Your score is {love_score}%.')
