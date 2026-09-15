class Sandwich:
    def __init__(self):
        self.bread: str | None = None
        self.meat: str | None = None
        self.cheese: str | None = None
        self.toppings = []
        self.sauces = []

    def __str__(self):
        return (f"Sandwich Config:\n"
                f"  Bread: {self.bread}\n"
                f"  Meat: {self.meat}\n"
                f"  Cheese: {self.cheese}\n"
                f"  Toppings: {', '.join(self.toppings) if self.toppings else 'None'}\n"
                f"  Sauces: {', '.join(self.sauces) if self.sauces else 'None'}")


class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()

    def set_bread(self, bread_type: str):
        self.sandwich.bread = bread_type
        return self 

    def set_meat(self, meat_type: str):
        # Step-by-step validation example
        if meat_type.lower() == "chicken" and self.sandwich.bread == "Gluten-Free":
            print("⚠️ Warning: Chicken marinade may contain gluten!")
        self.sandwich.meat = meat_type
        return self

    def set_cheese(self, cheese_type: str):
        self.sandwich.cheese = cheese_type
        return self

    def add_topping(self, topping: str):
        self.sandwich.toppings.append(topping)
        return self

    def add_sauce(self, sauce: str):
        self.sandwich.sauces.append(sauce)
        return self

    def build(self) -> Sandwich:
        if not self.sandwich.bread:
            raise ValueError("A sandwich must have bread!")
        
        return self.sandwich


if __name__ == "__main__":
    my_lunch = (
        SandwichBuilder()
        .set_bread("Sourdough")
        .set_meat("Turkey")
        .set_cheese("Swiss")
        .add_topping("Lettuce")
        .add_topping("Tomato")
        .add_sauce("Mayo")
        .build()
    )
    
    print(my_lunch)