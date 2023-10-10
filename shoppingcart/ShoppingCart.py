class Product:
    def __init__(self, name, price, quantity):
        # Initialize product attributes
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        # Initialize shopping cart attributes
        self.tax_rate = 0.1
        self.products = []

    def add_product(self, product):
        # Add a product to the cart
        self.products.append(product)
        print("\n" + product.name, "added.")

    def remove_product(self, product_name):
        # Remove a product from the cart by name
        for product in self.products:
            if product_name.lower() == product.name.lower():
                self.products.remove(product)
                print("\n" + product_name, "removed from cart.")
                return
        print("\n" + product_name, "not in cart.")

    def update_quantity(self, product_name, new_quantity):
        # Update the quantity of a product in the cart
        for product in self.products:
            if product_name.lower() == product.name.lower():
                index = self.products.index(product)
                self.products[index].quantity = int(new_quantity)
                print("\nQuantity updated.")
                return
        print("\n" + product_name, "does not exist.")

    def calculate_subtotal(self):
        # Calculate the subtotal of products in the cart
        sub = 0
        for item in self.products:
            if item.quantity > 0:
                sub += item.price * item.quantity
        return sub

    def set_tax_rate(self, tax_rate):
        # Set the tax rate for the cart
        self.tax_rate = float(tax_rate)

    def calculate_tax(self):
        # Calculate the total tax amount
        return self.tax_rate * self.calculate_subtotal()

    def calculate_total(self):
        # Calculate the total cost (subtotal + total tax)
        return self.calculate_subtotal() + self.calculate_tax()

    def display_cart(self):
        # Display all products in the cart with names, prices, and quantities
        print()
        for item in self.products:
            print(item.name + ":\nPrice = $" + str(item.price) + ", Quantity =", item.quantity)
        print("Current total: $" + str(round(self.calculate_subtotal(), 2)))

def main():
    # Create a ShoppingCart object
    shopping_cart = ShoppingCart()
    
    shopping_cart.add_product(Product("Apple", 1.0, 5))
    shopping_cart.add_product(Product("Banana", 0.5, 10))

    while True:
        print("\nShopping Cart Menu")
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. Update product quantity")
        print("4. Show all products in cart")
        print("5. Calculate total cost")
        print("6. Set tax rate")
        print("7. Calculate total tax")
        print("8. Quit")

        choice = input("\nEnter your choice: ")
        print()

        if choice == '1':
            # Add product to cart
            item = input("What product would you like to add to your cart?\n")
            shopping_cart.add_product(item)

        elif choice == '2':
            # Remove product from cart
            item = input("What product would you like to remove from your cart?\n")
            shopping_cart.remove_product(item)

        elif choice == '3':
            # Update product quantity
            item = input("What product would you like to update the quantity of?\n")
            quantity = input("\nWhat would you like to change the quantity of '" + item + "' to?\n")
            shopping_cart.update_quantity(item, quantity)

        elif choice == '4':
            # Display all products in cart
            shopping_cart.display_cart()

        elif choice == '5':
            # Calculate and display total cost
            shopping_cart.calculate_subtotal()
            print("\nCurrent total: $" + str(round(shopping_cart.calculate_subtotal(), 2)))

        elif choice == '6':
            # Set tax rate
            print("What would you like to set the tax rate for the cart as?")
            tax = input("Write this as a decimal (e.g., 0.08 for 8% tax):\n")
            shopping_cart.set_tax_rate(tax)
            print("\nTax updated.")

        elif choice == '7':
            # Calculate and display total tax
            print("\nTotal Cost: $" + str(round(shopping_cart.calculate_total(), 2)))

        elif choice == '8':
            print("Exiting the Shopping Cart.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
