









secret = 111
while 1:
    guess = int(raw_input("Unesi i probaj pogoditi broj: "))

    if guess == secret:
        print "Bravo, uspio si."
        break

    elif guess < secret:
        print "Nisi pogodio, tvoj broj je manji od tajnog."

    else:
        print "Nisi pogodio, tvoj broj je veci od tajnog."

