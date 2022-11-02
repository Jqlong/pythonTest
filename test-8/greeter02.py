def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("Please tell me your name:")
    f_name = input("First name:\n")
    if f_name == 'q':
        break;
    l_name = input("Last name:\n")
    if l_name == 'q':
        break;
    full_name = get_formatted_name(f_name,l_name)
    print(full_name)
    print(f"\nMaking a {full_name} -inch pizza with the following")

