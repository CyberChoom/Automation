def swap_numbers(list_name, number1, number2):
    list_name[number1], list_name[number2] = list_name[number2], list_name[number1]
    return list_name


list_x = [11, 33, 45, 99]
position1, position2 = 0, 2

print(swap_numbers(list_x, position1, position2))
