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
hasGiven = []     # empty list of people who have been assigned a giftee
hasReceived = []  # empty list of people who have been assigned a gifter
pairs = []        # pairs of gifter->giftee will be in this list
i=1               # cycle counter for logging
numberOfTries = [] #debug

for j in range(200):
    hasGiven = []     # reset because FAIL
    hasReceived = []  # reset because FAIL
    pairs = []        # reset because FAIL
    i=1
    while (len(hasGiven)!=len(people)):                     # loop until the number of people who have been assigned a giftee is the same number as the total people
        giver = people[random.randint(0,len(people)-1)]     # pick a random person as a try for gift giver
        receiver = people[random.randint(0,len(people)-1)]  # pick a random person as a try for gift receiver
        i+=1                                                # counter++

        if (len(hasGiven)==len(people)-1) and (len(hasReceived)==len(people)-1) and (giver==receiver): # FAIL: if the last remaining person to be picked for gifter has not yet been picked to be a giftee, they will necessarily pick themselves. FAIL
            hasGiven = []     # reset because FAIL
            hasReceived = []  # reset because FAIL
            pairs = []        # reset because FAIL
            print('FAIL')

        if (giver!=receiver) and (giver not in hasGiven) and (receiver not in hasReceived): # only when the picked giver and receiver are not the same, and they have not already been giver and receiver respectively
            pairs.append(giver+'--->'+receiver)             # add giver->receiver to pairs
            hasGiven.append(giver)                          # add giver to gifters list
            hasReceived.append(receiver)                    # add receiver to giftees list
            #log
            print('pair # '+str(i)+'is '+giver+'--->'+receiver)
    numberOfTries.append(i)


#################################################
print('')
print('printing pairs :')
for couple in range(len(pairs)):
    print(pairs[couple])
print('')
print('it took '+str(i)+' loops')

print(i)
print('THE BIG NUMBER IS '+str(sum(numberOfTries)/len(numberOfTries)) +"..."+str(len(numberOfTries)))
