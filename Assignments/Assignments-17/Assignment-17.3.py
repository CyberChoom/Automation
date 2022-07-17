# Exercise #1


my_list = []


def print_sum_avg(list):
    summary = 0
    count = 0
    for item in list:
        summary += item
        count += 1
    average = summary / count
    print(summary)
    print(average)


def input_and_result():
    print("3 numbers are needed to calculate the summary and the average")
    for item in range(3):
        user_input = int(input("Enter your number:\n"))
        my_list.append(user_input)
    print_sum_avg(my_list)


input_and_result()


# Exercise #2


def print_sum_avg_arg(*args):
    summary = 0
    count = 0
    for item in args:
        summary += item
        count += 1
    average = summary / count
    print(summary)
    print(average)


print_sum_avg_arg(3, 4, 5)


# Exercise #4


current_year = 2022
print("\nYou want to know how old you are but your math skills are not that great?\n")
user_input = input("No worries, just enter the year of your birth and "
                   "I'll tell you how old you really are \nfor a small price of your precious time!\n")
while int(user_input) > current_year or int(user_input) < 1910:
    print("Yea yea, tell me about it. I don't think you even exist, buddy.")
    user_input = input("Enter the TRUE year of your birth this time!\n")
age = str(current_year - int(user_input))
print("And your age is whopping " + age + " years! \nNo worries, you still have plenty of years to live. Hopefully.")
