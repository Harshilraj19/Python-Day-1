# pair delegates

import random
delegates = ["a","b","c","d","e"]

loop = 1
while len(delegates) > 2:
    del1 = random.choice(delegates)
    delegates.remove(del1)
    del2= random.choice(delegates)
    delegates.remove(del2)
    print(f" pair {loop} is {del1} and {del2}")
loop += 1
print(f" which leaves {delegates[0]} to join ")
