import random

def monty_hall(prize_amt=1000000, switch=False):
    doors = list(range(1, 4))
    prize = random.choice(doors)
    guess = random.choice(doors)
    if not switch:
        return prize_amt if prize == guess else 0
    reveal = random.choice([x for x in doors if x != guess and x != prize])
    guess = [x for x in doors if x != guess and x != reveal][0]
    return prize_amt if guess == prize else 0

#for i in range(10):
#    print(monty_hall())




for i in range(10):
    sum = 0
    for j in range(10):
        sum += monty_hall()
    print("not switch: %d" % sum)

for i in range(10):
    sum = 0
    for j in range(10):
        sum += monty_hall(switch=True)
    print("switch: %d" % sum)
