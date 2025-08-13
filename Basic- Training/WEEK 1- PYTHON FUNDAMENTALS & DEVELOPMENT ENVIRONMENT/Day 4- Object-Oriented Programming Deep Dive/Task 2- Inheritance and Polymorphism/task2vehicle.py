class Vehicle:
    """Base class for all vehicles."""

    def __init__(self, brand, model, year):
        """Initialize a generic vehicle."""
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        """Start the vehicle's engine."""
        return f"{self.brand} {self.model} engine started."

    def stop_engine(self):
        """Stop the vehicle's engine."""
        return f"{self.brand} {self.model} engine stopped."

    def display_info(self):
        """Display vehicle details."""
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    """Represents a car."""

    def __init__(self, brand, model, year, doors):
        """Initialize a car with number of doors."""
        super().__init__(brand, model, year)  # Call parent constructor
        self.doors = doors

    # Overriding method
    def display_info(self):
        return f"{super().display_info()} - {self.doors}-door car"


class Truck(Vehicle):
    """Represents a truck."""

    def __init__(self, brand, model, year, capacity_tons):
        """Initialize a truck with cargo capacity."""
        super().__init__(brand, model, year)
        self.capacity_tons = capacity_tons

    # Overriding method
    def display_info(self):
        return f"{super().display_info()} - Capacity: {self.capacity_tons} tons"


class Motorcycle(Vehicle):
    """Represents a motorcycle."""

    def __init__(self, brand, model, year, cc):
        """Initialize a motorcycle with engine size."""
        super().__init__(brand, model, year)
        self.cc = cc

    # Overriding method
    def display_info(self):
        return f"{super().display_info()} - {self.cc}cc engine"


# Multiple Inheritance Example
class Electric:
    """Mixin class for electric vehicles."""

    def charge_battery(self):
        return "Battery is charging."


class ElectricCar(Car, Electric):
    """Electric car that inherits from both Car and Electric."""
    pass


# Create different vehicles
vehicles = [
    Car("Toyota", "Camry", 2022, 4),
    Truck("Volvo", "FH16", 2021, 25),
    Motorcycle("Yamaha", "R1", 2023, 998),
    ElectricCar("Tesla", "Model S", 2024, 4)
]

# Loop through and call the same method
for v in vehicles:
    print(v.display_info())
    print(v.start_engine())
    if isinstance(v, Electric):
        print(v.charge_battery())  # Works for ElectricCar
    print("-" * 40)