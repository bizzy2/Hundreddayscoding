print('Welcome to the tip calculator')
bill = float(input('What was the total bill?: $'))
tip = int(input('What is the percentage tip would you like to give? 10, 12, or 15?: '))
split = int(input('How many people to split the bill?: '))


# Calculating tip percentage
def percentage_tip(x):
    actions = {
        x == 10: (bill) * .10,
        x == 12: (bill) * .12,
        x == 15: (bill) * .15
    }
    return actions.get(True, 'Please look at the tip range and input correctly')


tip_result = percentage_tip(tip)
Total_bill = bill + tip_result
print(f'Total to be paid is {Total_bill}')


# Calculating tip percentage
def percentage_tip(x):
    actions = {
        x == 10: (bill / split) * 1.10,
        x == 12: (bill / split) * 1.12,
        x == 15: (bill / split) * 1.15
    }
    return actions.get(True, 'Please look at the tip range and input correctly')


# Calculating split to be paid
output_split = percentage_tip(tip)
print(f'Each person should pay {output_split}')
