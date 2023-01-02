import random

client = input('Give me everyone\'s names, separated by a comma.')
client = client.split(',')

print(client)

# roulette = random.randint(0, len(client)-1)
# person_to_pay = client[roulette]
# Or
person_to_pay = random.choice(client)

print(f'The person to pay is {person_to_pay}')


