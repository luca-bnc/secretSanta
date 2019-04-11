import random
import pprint

people, forbiddenPairs, hasReceived, pairs = [   # list of all people
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
    'elena B',
    'daniela',
    'sara',
    'minivez',
    'jacopo'
], [['beppe', 'viviana'], ['elena B', 'daniela']], [], [] # illegal couples
i = 0
shit_happened = 0
random.shuffle(people)

while i != (len(people)):  # count until all the people are processed
    giver = people[i]
    try:
        receiver = random.choice(list(filter(lambda x: (x!=giver and (x not in hasReceived)), people))) #assign a random person to 'receiver' (that is not the same as giver, and not been assigned already)
    except IndexError: #if the last dude to pick can only pick himself
        shit_happened += 1 # oops counter
        pairs = []  # reset everything
        hasReceived = [] # reset everything
        i = 0 # start again from the first dude
        continue
    # TODO: qualche validazione su forbiddenPairs
    pairs.append([giver, receiver]) # write pair
    hasReceived.append(receiver)  # write down assigned receiver
    i+=1

pprint.pprint(pairs)
print('shit happened '+str(shit_happened) +' times')
