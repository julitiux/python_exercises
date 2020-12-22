def get_formatter_name(first_name, last_name):
    """Return a full_name , neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatter_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
