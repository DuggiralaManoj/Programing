
menu={
    "latte":{
        "ingredients":{
            "coffee":25,
            "milk":200,
            "water":100
        },
        "cost":200
        },
    "espresso":{
        "ingredients":{
            "coffee":30,
            "milk":250,
            "water":200
        },
        "cost":300
    },
    "cappuccino":{
        "ingredients":{
            "coffee":40,
            "milk":300,
            "water":100
        },
        "cost":400
    }

}

profit=0
resources={
    "coffee":200,
    "milk":1000,
    "water":800
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry, we don't have enough {item}")
            return False
    return True
def process_coins():
    print("Insert the coins:")
    total=0
    coins_five=int(input("How many 5rs. coins:"))
    coins_ten = int(input("How many 10rs. coins:"))
    coins_twenty = int(input("How many 20rs. coins:"))
    total=coins_five*5 +coins_ten*10 +coins_twenty*20
    return total

def is_payment_successful(money_inserted,coffee_cost):
    if money_inserted>=coffee_cost:
        global profit
        profit +=coffee_cost
        change=money_inserted-coffee_cost
        print(f"Take you change{change}")
        return True
    else:
        print("Sorry,thats not enough money, Money refunded.")
        return False

def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-=coffee_ingredients[item]
    print(f"Your  {coffee_name} is ready Enjoy it")

is_on=True
while is_on:
    choice=input("What would you like to have?(latte/espresso/cappuccino):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Coffee {resources['coffee']}g")
        print(f"Milk {resources['milk']}ml")
        print(f"Water {resources['water']}ml")
        print(f"Money Rs.{profit}")
    else:
        coffee_type=menu[choice]
        print(f"You chose {coffee_type}")
        if check_resources(coffee_type["ingredients"]):
            payment=process_coins()
            if is_payment_successful(payment,coffee_type["cost"]):
                make_coffee(choice,coffee_type["ingredients"],)

