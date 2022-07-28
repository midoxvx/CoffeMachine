from coffee import MENU, resources, coins

drink_list = ["espresso", "latte", "cappuccino"]


# TODO: 1. Build user prompt function "What would you like? (espresso/latte/cappuccino): " [X]
def main_prompt():
    return input(f"What would you like (espresso/latte/cappuccino)? ").lower()


# TODO: 2. Build in a report function that returns all resources [X]
def coffee_prompt_processor(user_input):
    """This is the main coffee function, takes user input (espresso, latte, cappuccino, off, report)"""
    if user_input == 'off':
        return 0
    elif user_input == 'report':
        print(resources)
    elif user_input in drink_list:
        if recipe_checker(user_input):
            coins_inserted = coin_processor()
            process_price(coins_inserted, user_input)
        return 10
    else:
        print("Wrong input")
        return 1


# TODO: 3. Build in an 'off' function keyword that turns off the coffee machine [X]

# TODO: 4. Check resources sufficient? if yes, proceed to coin process, if not exit
def recipe_checker(user_drink_choice):
    """Will take drink of choice as an input and check if there are enough resources in the coffee machine to prepare
    that drink"""
    ingredients_map = MENU[user_drink_choice]['ingredients']
    for ingredient, quantity in ingredients_map.items():
        if resources[ingredient] >= quantity:
            pass
        else:
            print(
                f"Insufficient resources, you need {quantity} of {ingredient} but you only have {resources[ingredient]}")
            return False
    return True


# TODO: 5. Process coins (Prompt for coins of all denominations)

def coin_processor():
    """This function will prompt the user to choose type and amount of coins to enter and will return total amount"""
    paid_amount = 0
    for denomination in coins:
        calculate = int(input(f"how many {denomination}? "))
        paid_amount += calculate * coins[denomination]
    return paid_amount


def resource_updater(flavor):
    """ Will take a flavor and return an updated dictionary of resources with new values"""
    ingredients_map = MENU[flavor]['ingredients']
    updated_resources = resources
    for ingredient in ingredients_map:
        updated_resources[ingredient] -= ingredients_map[ingredient]
    return updated_resources


# TODO: 7. Process price and return change
def process_price(total_payment, flavor):
    flavor_price = MENU[flavor]['cost']
    if total_payment >= flavor_price:
        print(f"Preparing coffee\nYour change will be: ${round(total_payment - flavor_price, 2)}")
        return 1
    else:
        print(f"Insufficient money, {flavor} costs: ${flavor_price}, you paid ${round(total_payment, 2)}")
        return 0


# TODO: 8. Make coffee & Update resources

power_switch = True
# TEST ZONE#

while power_switch:
    power_switch = coffee_prompt_processor(main_prompt())
