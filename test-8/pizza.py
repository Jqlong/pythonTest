def make_pizza(size,*toppings):
    print(f"Making a {size}-inch pizza with you,toppings:")
    for topping in toppings:
        print(f"- {topping}")