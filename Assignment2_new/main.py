import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(data.resources)
cashier_instance = Cashier()


def main():
    while True:
        size = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if size == "off":
            print("Machine is going to sleep. Ciao!")
            break
        elif size == "report":
            print("Machine resources report:")
            for ingredient, amount in sandwich_maker_instance.machine_resources.items():
                measurment = "slices" if ingredient in ["bread", "ham"] else "ounces"
                print(f"{ingredient.capitalize()}: {amount} {measurment}")
        elif size in ["small", "medium", "large"]:
            sandwich = recipes[size]

            # check for sufficient ingredients
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                money = cashier_instance.process_coins()

                if cashier_instance.transaction_result(money, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(size, sandwich["ingredients"])
        else:
            print("Invalid Entry. Try again")


if __name__ == "__main__":
    main()
