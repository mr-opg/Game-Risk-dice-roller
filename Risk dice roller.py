"""
This is a template script. Please work off of this.
To test the functionality of the script as you build
it, you can run this by opening a terminal, using 
"cd risk_project_fellow" and then running 
"python risk.py".

Your name: Overpower Gore
Your e-mail: mroverpowergore@gmail.com
Date finished: 9/26/2022
"""

# Step 1
# Collect the user's input. You can either use the
# argparse library for this (recommended) or the
# input() function.
import sys

for i in range(1000): # assuming every user will get the right instructions in the first 1000 times of trying 
    attackers = input("Number of attackers:")
    if attackers == "exit":
        sys.exit("Game aborted")
    defenders = input ("Number of defenders:")
    if defenders == "exit":
        sys.exit("Game aborted")
    threshold = input ("Number attack stops at:")
    if threshold == "exit":
        sys.exit("Game aborted")
    if int(threshold) > int(attackers):
        print("-----------------------------------------------------------------------------------------------------------")
        print("Number of units the attacker is willing is lose should be equal or less than the number of attacking units")
        print("Please input exit to quit the game at any moment")
        print("Please try again") #making sure the # of attackers is less than # of attackers willing to be lost
        print("-----------------------------------------------------------------------------------------------------------")
    else:
        break

attackers = int(attackers)
defenders = int(defenders)
threshold = int(threshold)
        
# Step 2
# Simulate dice rolls to determine the output.
import random

attackers_remaining = threshold
defenders_remaining = defenders
reserve = attackers - threshold

def attackers_function(attackers_remaining):    
    nums_attackers = [] # storing all the outcomes of the dice rolls 
    if attackers_remaining >= 3: #checking if we have at 3 units, if yes then we use all 3
        for i in range(3):
            dice = random.randint(1,6)
            nums_attackers.append(dice)
    elif attackers_remaining == 2: # checking if we have at 2 units, if yes then we use all 2
        for i in range(2):
            nums_attackers.append(random.randint(1,6))
    else:                        
        nums_attackers.append(random.randint(1,6))
    return nums_attackers

def defenders_function(defenders_remaining):    
    nums_defenders = []  # storing all the outcomes of the dice rolls
#     if defenders_remaining >= 3: #checking if we have at 3 units, if yes then we use all 3
#         for i in range(3):
#             dice = random.randint(1,6)
#             nums_defenders.append(dice)
    if defenders_remaining >= 2: # checking if we have at 2 units, if yes then we use all 2
        for i in range(2):
            nums_defenders.append(random.randint(1,6))
    else:
        nums_defenders.append(random.randint(1,6))
    return nums_defenders


for i in range(attackers_remaining+defenders_remaining):
    if defenders_remaining == 0: # if all defenders are lost then the attack won and the game is over
        break
    if attackers_remaining == 0: #if the attacker lost all the units its willing to lose then the game is over
        break
    dice_attackers = attackers_function(attackers_remaining)
    dice_defenders = defenders_function(defenders_remaining)
    if max(dice_attackers) > max(dice_defenders): #checking who won this round
        defenders_remaining -= 1
    else:
        attackers_remaining -= 1
    if len(dice_attackers) >=2 and len(dice_defenders) >= 2:
        dice_attackers.remove(max(dice_attackers))
        dice_defenders.remove(max(dice_defenders))
        if max(dice_attackers) > max(dice_defenders): #checking who won this round
            defenders_remaining -= 1
        else:
            attackers_remaining -= 1
    else:
        pass
        
attackers_remaining = attackers_remaining + reserve  


# Step 3
# Display the output to the user.
# To conform with our grader's required format, we've already 
# done this for you. Just make sure you set the number of 
# attackers remaining to the `attackers_remaining` variable and 
# the number of defenders remaining to the `defenders_remaining`
# variable in Step 2 of this script.

print(f"Attacker: {attackers_remaining} remaining; Defender: {defenders_remaining} remaining")
# print(
#     f"Attacker: {attackers_remaining} remaining; Defender: {defenders_remaining} remaining"
# )

# Step 4
# Run `python sanity_check.py` to confirm that your script
# handles inputs and outputs correctly