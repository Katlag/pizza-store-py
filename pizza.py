def get_name(pizzas):
    """Adds customers name to the finalised order

    Args:
        pizzas: Adds customer name to list

    Returns:
        list: listed in finalised order at the top of the list, and then name is reset
    """
    # Ask for customers name, will only accept a-z or A-Z, no spaces or special characters
    getting_name = True
    while getting_name:
        # Get the name, remove spaces, make the first letter caps
        customer_name = input("\nPlease enter your name: ").strip().title()
        if len(customer_name) < 2 or len(customer_name) > 20:
            #   Name can be no less than 2 characters and no more than 20 characters
            print("Please enter a name between 2-20 characters")
        elif customer_name.isalpha():  # Adds customer name to finalised order
            getting_name = False
        else:
            print("Please enter A-Z")
    return customer_name


def add_pizza(pizzas, pizza_menu):
    """Adds a single pizza to list/order
    Args:
        pizzas (list): Added to summary and finalised order
        pizza_menu: Taken from pizza menu and added to list
    Returns:
        pizzas: List of pizzas are updated
    """
    #   Adds a single pizza to the summary and finalised order
    print(pizza_menu)
    ordering_pizza = True
    while ordering_pizza:
        # Get the name of the pizza, remove spaces, make first letter caps
        print("****-Menu-****")
        for choice in pizza_menu:
            print(choice)
        ordering_pizza = input("\nPlease choose a pizza from the menu: ").strip().title()
        if ordering_pizza in pizza_menu:
            pizzas.append(ordering_pizza)  # Add a pizza to the list
            print("You have added a {} pizza to your order".format(ordering_pizza))
            ordering_pizza = False
        else:
            print("Sorry that is not on our menu, please pick another pizza")
        #   When a customer adds a pizza that is not on the menu it will come with an error message
        #   Will re-direct them back to the menu and question
    return pizzas


def add_multiple_pizza(pizza_menu, pizzas):
    """Adds multiple pizzas to list/order
        Args:
            pizzas (list): Added to summary and finalised order
            pizza_menu: Taken from pizza menu and added to list
        Returns:
            pizzas: List of pizzas are updated
        """
    #   Asks for number of pizzas customer wants to order
    count = 0
    getting_multi_pizza = True
    while getting_multi_pizza:
        getting_num_pizza = True
        while getting_num_pizza:
            try:
                how_many_pizza = int(input("\nHow many pizza's do you want to order? "))
                getting_num_pizza = False
            except ValueError:
                print("Please enter a number between 1-10")

        #   Makes sure customer orders the right amount of pizzas
        if how_many_pizza > 10:
            print("Your order can not have over 10 pizzas.")
            #   If someone puts in a number over 10, this error message will come up
        elif how_many_pizza == 0:
            #   If someone orders 0 pizza's this error message will come up
            print("Your order can not have 0 pizzas.")
        else:
            print("****-Menu-****")
            for choice in pizza_menu:
                print(choice)

            #   Asks for what pizza customer wants to order
            while count < how_many_pizza:
                pizza_name = input("\nPlease enter a pizza choice from menu {}: ".format(count + 1)).strip().title()
                if pizza_name in pizza_menu:
                    pizzas.append(pizza_name)
                    count += 1
                    getting_multi_pizza = False
                #   Pizza not on the menu will come up with an error message
                else:
                    print("Sorry, that is not on our menu, please choose another pizza.")
                    print("****-Menu-****")
                    for choice in pizza_menu:
                        print(choice)
    return pizzas


def remove_pizza(count_pizza, pizza_menu, pizzas):
    """Deletes a pizza from your list
    Args:
        pizzas (list): The list of pizzas
        count_pizza: Removes one less pizza from list
        pizza_menu: Removes pizza you previously selected from menu
    Returns:
        list: List of pizzas, updated
    """
    if len(pizzas) == 0:  # Check there are pizza's in the list.
        print("\nThere are no pizza's on your list")
    else:
        removing_pizza = True
        while removing_pizza:
            # Get the name of pizza, remove spaces, make first letter caps
            pizza_to_remove = input("\nPlease enter the name of the pizza you would like to remove: ").strip().title()
            # Check if the pizza exists in the list
            if pizza_to_remove in pizza_menu:
                pizzas.remove(pizza_to_remove)  # Remove pizza from the list
                count_pizza -= 1
                print("You have removed a {} pizza from your order".format(pizza_to_remove))
                removing_pizza = False
            else:
                print("\nSorry, you do not have a {} pizza in your order".format(pizza_to_remove))
    return pizzas


def pizza_summary(pizzas, customer_name):
    """Prints out a nicely formatted summary of the pizzas ordered
    Args:
        pizzas(list): The list of pizzas ordered
    """

    if len(customer_name) == 0:
        print("Please enter a name first")

    if len(pizzas) > 0:  # Only print if there are pizza's on the list
        print("Here are the pizza's you have selected: ")
        for pizza in pizzas:
            print("- {}".format(pizza))  # List of pizza's will be printed out
    return pizzas


def finalise_order(pizzas, customer_name):
    """Prints out customer name, list of pizzas ordered and total cost, alphabetizes list
    Args:
        pizzas(list): The list of pizzas
        customer_name: Adds customer name at the top of the order
    Returns:
        list: Clears order, list of pizzas and customer name

    """

    if len(customer_name) == 0:
        print("Please enter a name first")

    if len(pizzas) == 0:
        print("You must enter a pizza before accessing the summary")

    else:
        pizzas.sort()  # Alphabetizes pizzas on list
        total_cost = len(pizzas) * 20
        print("***-{}'s order-***".format(customer_name))
        print("- {}".format(pizzas))
        print("Total cost of pizza's = ${}".format(total_cost))
        print("Your order had been finalised")

    customer_name = ""  # Reset the customers name
    pizzas = []  # Reset the pizza's ordered
    count_pizza = 0  # Reset the price of all pizza's
    return pizzas


def main():
    count_pizza = 0
    customer_name = ""
    pizza_menu = ["Hawaiian", "Cheese", "Pepperoni", "Ham", "Vegetarian"]
    pizzas = []

    while True:
        #   Give the user a list, only accept numeric input
        getting_option = True
        while getting_option:
            try:
                option = int(input("\n1) Enter your name\n"
                                   "2) Add a pizza\n"
                                   "3) Add multiple pizza's\n"
                                   "4) Remove a pizza\n"
                                   "5) Summary\n"
                                   "6) Finalise your order\n"
                                   "7) Exit\n"
                                   "Your choice: "))
                getting_option = False

            except ValueError:
                print("\nPlease enter a number between 1-7. ")

        if option == 1:
            customer_name = get_name(pizzas)

        elif option == 2:
            pizzas = add_pizza(pizzas, pizza_menu)

        elif option == 3:
            pizzas = add_multiple_pizza(pizza_menu, pizzas)

        elif option == 4:
            pizzas = remove_pizza(count_pizza, pizza_menu, pizzas)

        elif option == 5:
            pizzas = pizza_summary(pizzas, customer_name)

        elif option == 6:
            pizzas = finalise_order(pizzas, customer_name)

        elif option == 7:
            print("Thank your for your order, enjoy your day. ")
            exit()  # Ends program with a short message

        else:
            print("\nPlease enter a number between 1 and 7: ")


main()
