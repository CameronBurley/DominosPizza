from pizzapy import Customer, StoreLocator, Order, ConsoleInput
TAXRATE = 1.0725

def search_menu(menu):
    print("You are now searching the menu...")
   
    item = input("Type in item to look for: ").strip().lower()

    if len(item) > 1:
        item = item[0].upper() + item[1:]
        print("")
        print(f"Resultes for: {item}")
        menu.search(Name=item)
    else:
        print("No Results")

def add_to_order(order):
    print("Please type the codes of the items you'd like to order..")
    print("Press ENTER to stop ordering.")
    while True:
        item = input("Code: ").upper()    
        try:
            order.add_item(item)
        except:
            if item == "":
                break
            print("Invalid Code...")


customer = ConsoleInput.get_new_customer()

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
print("\nClosest Store: ")
print("")
print(my_local_dominos)

ans = input("Would you like to order from this store? (y/n)")
if ans.lower in ["no", "n"]:
    print("Goodbye!")
    quit()
print("\nMenu\n")

menu = my_local_dominos.get_menu()
order = Order.begin_customer_order(customer, my_local_dominos)

while True:
    search_menu(menu)
    add_to_order(order)
    answer = input("Would you like to add more items (y/n? ")
    if answer.lower() in ["no", "n"]:
        break

print("\nYour order is as follows: ")

total = 0
for item in order.data["Products"]:
    price = item["Price"]
    print(item["Name"] + " $" + price)
    total += float(price)

total *= TAXRATE

print("\nYour order total is: $" + "{:.2f}\n".format(total))
payment = input("Will you be paying CASH or CREDIT? ")
if payment.lower() in ["card","credit card"]:
    card = ConsoleInput.get_credit_card()
else:
    card = False

ans = input("Would you like to place this order? (y/n)")
if ans.lower() in ["y", "yes"]:
    order.place(card)
    my_local_dominos.place_order(order, card)
    print("Order Placed!")
else:
    print("Goodbye")





