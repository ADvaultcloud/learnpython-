menu = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 20
    },
    "cost": 50
  },
  "latte": {
    "ingredients": {
      "water": 60,
      "milk": 100,
      "coffee": 40
    },
    "cost": 80
  },
  "cappuccino": {
    "ingredients": {
      "water": 40,
      "milk": 150,
      "coffee": 50
    },
    "cost": 100
  }
}

   


resources={
    "water": 500,
    "milk": 1000,
    "coffee":500
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
        
    return True


def process_money():
    print("Please insert the cash ")
    total = int(input(" How many 10 rupees:")) * 10
    total += int(input(" How many 20 rupees:")) * 20
    total += int(input(" How many 50 rupees:")) * 50
    total += int(input(" How many 100 rupees:")) * 100
    return total

def is_transaction_successful(money_recieved,drink_cost):
    if money_recieved >= drink_cost:
        change=round(money_recieved - drink_cost,2)
        print(f"Here is Rs{change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry insufficient cash to continue, Money refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]=order_ingredients[item]
    print(f"Here is your drink {drink_name}")    




profit = 0 
is_on =True
while is_on:
    choice = input("What would you like to have?('espresso'/'latte'/'cappucinno')")
    if choice == "off":
        is_on = False
        print("Turning off the machine")
    elif choice == "report":
       print(f"water : {resources["water"]}ml")
       print(f"milk : {resources["milk"]}ml")
       print(f"coffee : {resources["coffee"]}gm")
       print(f"money : Rs{profit}")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_money()
            is_transaction_successful(payment,drink["cost"])  
            make_coffee(choice,drink["ingredients"])
