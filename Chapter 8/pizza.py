def make_pizza(size, *toppings):
    """Print the list of toppings that hace been request"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

#make_pizza('pepperoni')
#make_pizza('mushrooms','green peppers','extra cheese')
