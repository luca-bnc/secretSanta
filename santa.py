import random

people = [   #list of all people
    'luca',
    'elia',
    'camilla',
    'viviana',
    'beppe',
    'leo',
    'gio',
    'gabri',
    'cabe',
    'stefano',
    'elena N',
    'elena B',
    'daniela',
    'sara',
    'minivez',
    'jacopo'
]
hasGiven, hasReceived, pairs = [], [], [] # empty lists
i=1                # cycle counter for logging
numberOfTries = [] #debug

while (len(hasGiven)!=len(people)): # loop until the number of people who have been assigned a giftee is the same number as the total people

    receiver = giver = random.choice(people) # set receiver and giver to same person and then
    while receiver == giver:                 # loop until they are different
        receiver = random.choice(people)
        i+=1
        if (giver != receiver) and (giver not in hasGiven) and (receiver not in hasReceived): #if dudes have not already been giver and receiver respectively
            pairs.append(giver+'--->'+receiver)             # add 'giver->receiver' to pairs
            hasGiven.append(giver)                          # add giver to gifters list
            hasReceived.append(receiver)                    # add receiver to giftees list
            break
        else:
            continue

print('printing pairs:')
for couple in range(len(pairs)):
    print(pairs[couple])
print('it took '+str(i)+' loops')
