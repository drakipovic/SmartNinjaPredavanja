from random import randint

secret = randint(0, 100)
print secret


guess = raw_input("Odaberi broj: ")

if secret == guess:
    print "Odabrani broj je tocan, bravo."

else:
    print "Odabrani broj nije tocan, probaj opet."