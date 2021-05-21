import random
import numpy as np
import ap_stats

def monty_hall(prize_amt=1, switch=False):
    doors = list(range(1, 4)) # enumerate the doors
    prize = random.choice(doors) # randomly choose the prize location
    guess = random.choice(doors) # randomly choose the guess location
    
    # if not switching, we're done. if correct, return the prize, otherwise zero.
    if not switch:
        return prize_amt if prize == guess else 0 
    
    # randomly choose a door that does not contain the prize
    reveal = random.choice([x for x in doors if x != guess and x != prize])
    
    # switch to the last remaining door.
    guess = [x for x in doors if x != guess and x != reveal][0]
    
    # if correct return the prize, otherwise, zero.
    return prize_amt if guess == prize else 0

def run_sim(num_batches=25, batch_size=10, switch=False):
    results = np.zeros(num_batches, int)
 
    for i in range(num_batches):
        for j in range(batch_size):
            results[i] += monty_hall(switch=switch)
            
    title = "{} Simulation (num_batches = {}, batch_size = {})".format( 
                "Switch" if switch else "Stay",
                num_batches, 
                batch_size)
  
    ap_stats.dotplot(data=results, 
                     keys=range(1, 11), 
                     num_stacks=batch_size, 
                     title = title,
                     ylabel="# of Occurances",
                     xlabel="Amount Won Per Batch", 
                     filename = "switch.png" if switch else "stay.png")

run_sim(switch=False)
run_sim(switch=True)