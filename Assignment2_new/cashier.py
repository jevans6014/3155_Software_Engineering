class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        input("Please enter coins to pay: ")
        large_d = int(input("How many large dollar bills are you entering ($1): "))
        half_d = int(input("How many half dollar bills are you entering ($0.50): "))
        quarters = int(input("How many quarters are you entering ($0.25): "))
        nickels = int(input("How many nickels are you entering ($0.05): "))
        total = (large_d * 1) + (half_d * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins < cost:
            print("You do not have enough money. Please take your money back")
            return False
        elif coins > cost:
            change = round(coins-cost, 2)
            print(f"Take your change of {change}")
            return True
        else:
            print("Wow exact amount of money! There is $0.0 in change.")
            return True

