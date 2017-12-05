print "Welcome to the todo managment program!"

f = open("todo.txt", "a")

f.write("Task name     Is it done?\n")
f.write("-------------------------\n")

while True:
    task = raw_input("Please enter your task: ")

    print "Your task is", task

    is_done = raw_input("Is this task done? [yes/no]")

    if is_done == "yes":
        f.write(task + "     " + "DONE\n")

    else:
        f.write(task + "     " + "NOT DONE\n")

    new_task = raw_input("Do you want to enter new task? [yes/no]")

    if new_task == "no":
        break


f.close()