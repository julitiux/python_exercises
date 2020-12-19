request_topping = 'mushrooms'

if request_topping != 'anchovies':
    print("Hold the anchovies")


request_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in request_toppings:
    print("Adding mushrooms.")
if 'pepperonu' in request_toppings:
    print("Adding mushrooms.")
if 'extra cheese' in request_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


request_toppings = ['mushrooms','extra cheese','green peppers']

for request_topping in request_toppings:
    print("Adding " + request_topping + ".")

print("\nFinished making your pizza!")
