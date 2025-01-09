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

# Initial resource quantities
resource = {'Water': 300,
            'Milk': 200,
            'Coffee': 100
            }

# Coin values in cents
coins = { 
    'quarter': 25,
    'dimes': 10,
    'nickles': 5,
    'pennies': 1
}

# Function to check if resources are sufficient for the selected coffee
def check_resource_sufficient(selected_coffee):
    if MENU[selected_coffee]['ingredients']['water'] > resource["Water"]:
        print("Sorry there is not enough water.")
    elif MENU[selected_coffee]['ingredients']['coffee'] > resource["Coffee"]:
        print("Sorry there is not enough coffee.")
    elif 'milk' in MENU[selected_coffee]['ingredients'] and MENU[selected_coffee]['ingredients']['milk'] > resource["Milk"]:
        print("Sorry there is not enough milk.")

# Function to check if the transaction was successful
def check_transaction_successful(selected_coffee, total_amount):
    if total_amount < MENU[selected_coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 1
    return 0

# Function to deduct resources used for the selected coffee
def make_coffee(coffee):
    resource["Water"] -= MENU[coffee]['ingredients']['water']
    if 'milk' in MENU[coffee]['ingredients']:
        resource["Milk"] -= MENU[coffee]['ingredients']['milk']
    resource["Coffee"] -= MENU[coffee]['ingredients']['coffee']

# Function to process coin input and return total money inserted
def process_coin(selected_option):
    print("Please insert coins.")
    total_coin = 0
    quarter = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total_coin = (coins['quarter'] * quarter) + (coins['dimes'] * dimes) + (coins["nickles"] * nickles) + (coins["pennies"] * pennies)
    total_value = total_coin / 100  # Convert cents to dollars
    if check_transaction_successful(selected_option, total_value):
        return 0
    else:
        make_coffee(selected_option)
        change = total_value - MENU[selected_option]["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {selected_option}. Enjoy!")
        return MENU[selected_option]["cost"]

# Initialize profit and loop control variable
profit = 0
is_stop = False

# Main loop for the coffee machine operation
while not is_stop:
    user_SelectedOption = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_SelectedOption == 'report':
        # Print current resource status
        print(f"Water: {resource['Water']}ml\nMilk: {resource['Milk']}ml\nCoffee: {resource['Coffee']}g\nMoney: ${profit:.2f}")
    elif user_SelectedOption in ['latte', 'espresso', 'cappuccino']:
        # Check resource and process coin for selected coffee
        check_resource_sufficient(user_SelectedOption)
        profit += process_coin(selected_option=user_SelectedOption)
    elif user_SelectedOption == 'off':
        # Turn off the machine
        is_stop = True
