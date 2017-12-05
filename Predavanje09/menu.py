
f = open("menu.txt", "a")

day = raw_input("Please enter what day is today - ")
f.write(day + ":\n")

dish_name = raw_input("Please enter dish name: ")
f.write(dish_name + " : ")

dish_price = raw_input("Please enter dish price: ")
f.write(dish_price + "\n")

f.write("-"*20 + "\n")