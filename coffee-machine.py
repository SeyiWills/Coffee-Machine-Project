from main import MENU
from main import resources

#if there is not enough resources to make a drink it returns a message
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
#this checks to see if there is enough resources left in the coffee maker
def can_make_any_drink():
    for drink in MENU.values():
        if check_resources(drink["ingredients"]):
            return True
    return False
can_make_any_drink()   


def coffee_maker():
#Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    global resources
    #global order

while can_make_any_drink():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if order == "off":
        exit()
    
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")  
    
    # Check the user's input to decide what to do next
    elif order in MENU:
        drink = MENU[order]
        
        # Check if there are enough resources to make the drink
        if check_resources(drink["ingredients"]):
            print(f"The cost is: ${drink['cost']}")
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            
            # Calculate total coins inserted
            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            
            if total >= drink["cost"]:
                change = round(total - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {order}. Enjoy!")
                
                # Deduct the resources
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                
                resources["money"] += drink["cost"]
                    
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            # Not enough resources, message is already printed in check_resources()
            pass   
    
print("Sorry, there are not enough resources to make any drink")

coffee_maker()  









    
    

