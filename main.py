MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

total_user_money = 0


def check_resources(selected_coffee):
    enough_resources = True

    for item in MENU[selected_coffee]['ingredients']:
        if resources[item] <= MENU[selected_coffee]['ingredients'][item]:
            enough_resources = False

    return enough_resources


def ask_money():
    print("Please insert coins")

    ok_quarters = False
    while ok_quarters == False:
        user_quarters = input("How many quarters? ")
        if user_quarters.isdigit() == True:
            ok_quarters = True
            user_quarters = int(user_quarters)
        else:
            print("Please type in an integer")

    ok_dimes = False
    while ok_dimes == False:
        user_dimes = input("How many dimes? ")
        if user_dimes.isdigit() == True:
            ok_dimes = True
            user_dimes = int(user_dimes)
        else:
            print("Please type in an integer")

    ok_nickles = False
    while ok_nickles == False:
        user_nickles = input("How many nickles? ")
        if user_nickles.isdigit() == True:
            ok_nickles = True
            user_nickles = int(user_nickles)
        else:
            print("Please type in an integer")

    ok_pennies = False
    while ok_pennies == False:
        user_pennies = input("How many pennies? ")
        if user_pennies.isdigit() == True:
            ok_pennies = True
            user_pennies = int(user_pennies)
        else:
            print("Please type in an integer")

    # quarter = $0.25 // dime = $0.10 // nickle = $0.05 // penny = $0.01
    total_money = round(((user_quarters * 0.25) + (user_dimes * 0.1) + (user_nickles * 0.05) + (user_pennies * 0.01)), 2)

    return total_money


def buy_coffee(selected_coffee):
    global ok_answer_2
    global total_user_money

    total_user_money += ask_money()

    print(f"Your total money is: ${round(total_user_money, 2)}")

    if MENU[selected_coffee]['cost'] <= total_user_money:

        resources['water'] -= MENU[selected_coffee]['ingredients']['water']
        resources['coffee'] -= MENU[selected_coffee]['ingredients']['coffee']
        resources['milk'] -= MENU[selected_coffee]['ingredients']['milk']

        user_change = total_user_money - MENU[selected_coffee]['cost']

        resources['money'] += MENU[selected_coffee]['cost']

        print(f"Here is ${round(user_change, 2)} in change")
        print("Thanks for your purchase. Here is your coffee: ☕️")

        ok_answer_2 = True
        total_user_money = 0

    else:
        return False


def start():
    global ok_answer_2

    ok_answer_1 = False
    while ok_answer_1 == False:

        user_welcome_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_welcome_input in ("espresso", "latte", "cappuccino"):
            print("** Your answer is valid")

            user_coffee = user_welcome_input

            if check_resources(user_coffee) == True:

                if buy_coffee(user_coffee) == False:

                    ok_answer_2 = False
                    while ok_answer_2 == False:
                        user_lacks_money_input = input(
                            "We're sorry, you haven't inserted enough money to purchase your product. Type 'M' to add "
                            "more money or 'S' to choose another product ")

                        if user_lacks_money_input in ('M', 'm'):
                            buy_coffee(user_coffee)

                        elif user_lacks_money_input in ('S', 's'):
                            ok_answer_2 = True
            else:
                print("We're sorry. The machine does not count with enough resources to prepare your order. Choose a "
                      "different product.")

        elif user_welcome_input == "report":
            print(f"""        
            Water: {resources["water"]}ml
            Milk: {resources["milk"]}ml
            Coffee: {resources["coffee"]}g
            Money: ${resources["money"]}
            """)

        elif user_welcome_input == "off":
            print("Ok! See you later...")
            ok_answer_1 = True

        else:
            print("     Please type a valid answer")

start()

'''
# TO DO 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#   1.a Check the user’s input to decide what to do next.
#   1.b The prompt should show every time action has completed. The prompt should show again to serve the next customer.
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
#   2.a For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
# TODO 3. Print report. a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
# TODO 4 Check resources sufficient?
#   4.a When the user chooses a drink, the program should check if there are enough resources to make that drink.
#   4.b E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
#   4.c The same should happen if another resource is depleted, e.g. milk or coffee.
# TODO 5. Process coins.
#   5.a If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
#   5.b Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#   5.c Calculate the monetary value of the coins inserted. Example: 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# TODO 6 Check transaction successful?
#   6.a Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
# TODO 7 But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g. Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
# TODO 8.c If the user has inserted too much money, the machine should offer change.
'''