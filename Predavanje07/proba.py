x = float(raw_input("Prvi broj: "))

operation = raw_input("Koju operaciju zelis? Mogucnosti su + - / * **: ")

y = float(raw_input("Drugi broj: "))


if operation == '+':
    print x + y

elif operation == '-':
    print x - y

elif operation == '*':
    print x * y

elif operation == "**":
    print x ** y

else:
    print x / y
