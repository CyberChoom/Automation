# Exercise #1

while True:
    user_input = input("Type away, my friend:\n")
    if user_input == "STOP":
        break
    elif user_input != "STOP":
        print(user_input.lower())

# Exercise #2

dic = {'Jake': '$100K', 'Anand': '$120K'}
print("Jake's salary is {Jake}, Anand's salary is {Anand}.".format(**dic))

# Exercise #3

tup = (4, 30, 2017, 2, 27)
print("{} {} {} {} {}".format(tup[3], tup[4], tup[2], tup[0], tup[1]))
