print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit")
while True:
    first_num = input("First number:\n")
    if first_num == 'q':
        break
    second_num = input("Second number:\n")
    if second_num == 'q':
        break
    try:
        res = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by 0")
    else:
        print(res)