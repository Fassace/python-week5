# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = price  # Encapsulation: price is "protected"

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self._price}")

    def make_call(self, number):
        print(f"{self.model} is calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: '{message}'")

    # Getter for price (demonstrating encapsulation)
    def get_price(self):
        return self._price

    # Setter for price (allowing controlled modification)
    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Invalid price. Price must be greater than 0.")

# Derived class: Smartphone with Camera
class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels

    # Polymorphism: Overriding display_info method
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self._price}, Camera: {self.camera_megapixels}MP")

    def take_photo(self):
        print(f"{self.model} took a photo with its {self.camera_megapixels}MP camera.")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S21", 999)
phone2 = CameraSmartphone("Apple", "iPhone 14 Pro", 1299, 48)

# Display information
phone1.display_info()
phone2.display_info()

# Demonstrate methods
phone1.make_call("123-456-7890")
phone2.take_photo()

# Encapsulation example
print(f"Original price of {phone1.model}: ${phone1.get_price()}")
phone1.set_price(899)
print(f"Updated price of {phone1.model}: ${phone1.get_price()}")
