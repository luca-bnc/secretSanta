import random

people = [   # list of all people
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

while (len(hasGiven)!=(len(people))): #loop until all people have been assigned a giftee
    i+=1                              # iteration counter
    giver = random.choice(people)     # pick random dude for gifter
    receiver = giver                  # assign same dude for receiving gift

    while (receiver == giver):        # continue picking receiver until the 2 dudes are different dudes
        receiver = random.choice(people)

    if ((receiver in hasReceived) or (giver in hasGiven)): # if the 2 dudes have already been picked for their respective role, start again
        continue

    pairs.append([giver, receiver]) # write the couple in list
    hasGiven.append(giver) # write down that gifter dude is confirmed as gifter
    hasReceived.append(receiver) # write down that receiving dude is confirmed as receiver

    if (len(hasGiven)==len(people)-1): # when only one dude is left to pick from hat, do this check
        hasGiven.sort() # i need this to compare lists..
        hasReceived.sort() # i need this to compare lists..
        if(hasReceived==hasGiven): # if final dude picks himself from hat, then tough shit:
            hasGiven, hasReceived, pairs = [], [], [] # all dudes have to start again

print('printing pairs:')
for couple in range(len(pairs)):
    print(pairs[couple])
print('it took '+str(i)+' loops')
##
