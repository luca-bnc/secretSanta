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
], [['beppe', 'viviana'], ['elena B', 'daniela']], [], []
i = 0
shit_happened = 0
random.shuffle(people)

while i != (len(people)):
    giver = people[i]
    try:
        receiver = random.choice(list(filter(lambda x: (x!=giver and (x not in hasReceived)), people)))
    except IndexError:
        shit_happened += 1
        pairs = []
        hasReceived = []
        i = 0
        continue
    # TODO: qualche validazione su forbiddenPairs
    pairs.append([giver, receiver])
    hasReceived.append(receiver)
    i+=1


pprint.pprint(pairs)
print('shit happened '+str(shit_happened) +' times')
