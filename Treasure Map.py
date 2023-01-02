"""
row1 = ['⬜', '⬜', '⬜']
row2 = ['⬜', '⬜', '⬜']
row3 = ['⬜', '⬜', '⬜']
content = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
choice = input('where do you want to put the treasure?')
choice_1 = int(choice[1])
choice_2 = int(choice[0])
content[choice_2-1][choice_1-1] = 'X'
print(choice)
print(f'{row1}\n{row2}\n{row3}')

"""
row1 = ['⬜', '⬜', '⬜']
row2 = ['⬜', '⬜', '⬜']
row3 = ['⬜', '⬜', '⬜']
content = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
choice = input('where do you want to put the treasure?\n')
row, col = map(int, choice)
content[row-1][col-1] = 'X'
print(f'{row1}\n{row2}\n{row3}')

