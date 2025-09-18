
def make_pizza(size, *toppings):
    "Summarize the pizza we are about to make."
    print(f"\nMaking a {size}-inch pizza with following toppings:")
    for all_toppings in toppings:
        print(f"- {all_toppings}")