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
], [('beppe', 'viviana'), ('elena B', 'daniela')], [], []

for giver in people:
    try: # for each person, pick a random dude that is not themselves and that has not yet been picked
        receiver = random.choice(list(filter(lambda x: x!= giver and x not in hasReceived, people)))
    except IndexError:
        continue # if last dude has no choice but to pick himself, start again

    if ((giver, receiver) in forbiddenPairs or (receiver, giver) in forbiddenPairs):
        giver = people.index(giver)-1 # if pairing is forbidden, draw (only that pair) again

    hasReceived.append(receiver) # log that the dude has been picked for receiving, so that they won't be picked again
    pairs.append((giver, receiver)) # append succesful pairs

pprint.pprint(pairs)
