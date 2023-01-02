import random

comp = random.randint(0, 2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

select = [rock, paper, scissors]
value = int(input('What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: '))

'''
if value == comp:
    print('Try again')
    print(f'you choose {select[value]}')
    print(f'comp choose {select[comp]}')
elif value == 0 and comp == 2:
    print('You win')
    print(f'you choose {select[value]}')
    print(f'comp choose {select[comp]}')
elif value == 2 and comp == 1:
    print('You win')
    print(f'you choose {select[value]}')
    print(f'comp choose {select[comp]}')
elif value == 1 and comp == 0:
    print('You win')
    print(f'you choose {select[value]}')
    print(f'comp choose {select[comp]}')
else:
    print('You loose')
    print(f'you choose {select[value]}')
    print(f'comp choose {select[comp]}')
'''
if value == comp:
    print('Try again')
elif (value == 0 and comp == 2) or (value == 2 and comp == 1) or (value == 1 and comp == 0):
    print('You win')
else:
    print('You loose')
print(f'you choose {select[value]}')
print(f'comp choose {select[comp]}')

