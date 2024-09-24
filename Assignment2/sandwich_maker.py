
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if self.machine_resources[ingredient] < ingredients[ingredient]: # compares ingrediesnts you have vs. required
                print(f"You do not have enough {ingredient} silly!")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient in order_ingredients:
            self.machine_resources[ingredient] -= order_ingredients[ingredient]
        print(f"{sandwich_size} is ready. Bon appetit!")