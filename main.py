MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

profit = 0

def isEnoughResource(orderIngredients):
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def isTransaction_successful(customer_money, drink_cost):
    if customer_money >= drink_cost:
        change = round(customer_money - drink_cost, 2)
        print(f"Here is your ${change} change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry insufficient funds, money refunded.")
        return False


# Prompt user
turnOnCoffeMachine = True

while turnOnCoffeMachine: 
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        turnOnCoffeMachine = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: £{profit}")

# check resuource sufficient
    else:
        drink = MENU[choice]
        if isEnoughResource(drink["ingredients"]):

# process coins
            payment = process_coins()

#check transaction successful
            isTransaction_successful(payment, drink["cost"])