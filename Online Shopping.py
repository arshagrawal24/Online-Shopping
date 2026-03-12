import sys

# 1. Product Catalog: A dictionary where the key is the Item ID (number)
# and the value is a dictionary containing item details.
PRODUCT_CATALOG = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Mechanical Keyboard", "price": 75.50},
    3: {"name": "Gaming Mouse", "price": 35.00},
    4: {"name": "Webcam", "price": 55.99},
    5: {"name": "Monitor (27-inch)", "price": 249.99}
}

# 2. Shopping Cart: A dictionary to store items the user adds.
# Key: Item ID (integer)
# Value: Quantity (integer)
shopping_cart = {}

# --- Utility Functions ---

def display_products():
    """Displays the current product catalog to the user."""
    print("\n" + "="*40)
    print("           Product Catalog")
    print("="*40)
    print("ID | Item Name              | Price")
    print("-" * 40)
    for item_id, details in PRODUCT_CATALOG.items():
        name = details["name"].ljust(20)  # Left-justify name for clean columns
        price = f"{details['price']:.2f}"
        print(f"{item_id:<2} | {name} | {price}")
    print("-" * 40)

def add_to_cart():
    """Allows the user to select a product and quantity to add to the cart."""
    display_products()

    while True:
        try:
            item_id = int(input("Enter the ID of the item you want to add (or 0 to cancel): "))
            if item_id == 0:
                return

            if item_id in PRODUCT_CATALOG:
                # Get the selected product details
                product = PRODUCT_CATALOG[item_id]
                print(f"Selected: {product['name']} (${product['price']:.2f})")

                # Get quantity
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                # Update the cart
                if item_id in shopping_cart:
                    shopping_cart[item_id] += quantity
                else:
                    shopping_cart[item_id] = quantity

                print(f"\n {quantity} x {product['name']} added to your cart.")
                break
            else:
                print(" Invalid item ID. Please try again.")

        except ValueError:
            print(" Invalid input. Please enter a number for the ID and quantity.")

def view_cart():
    """Displays the current contents of the shopping cart and calculates the subtotal."""
    print("\n" + "="*50)
    print("           YOUR SHOPPING CART")
    print("="*50)

    if not shopping_cart:
        print("Your cart is empty. Time to shop!")
        print("="*50)
        return 0.0

    subtotal = 0.0
    print("Qty | Item Name              | Unit Price | Line Total")
    print("-" * 50)

    for item_id, quantity in shopping_cart.items():
        # Retrieve product details from the catalog
        product = PRODUCT_CATALOG[item_id]
        line_total = product["price"] * quantity
        subtotal += line_total

        name = product["name"].ljust(20)
        unit_price = f"{product['price']:.2f}"
        line_total_str = f"{line_total:.2f}"

        print(f"{quantity:<3} | {name} | {unit_price:<10} | {line_total_str}")

    print("-" * 50)
    print(f"Subtotal: {'':<31} {subtotal:.2f}")
    print("="*50)
    return subtotal

def checkout():
    """Calculates the final total (including a simple tax) and confirms the order."""
    subtotal = view_cart()

    if subtotal == 0.0:
        print("Cannot checkout with an empty cart.")
        return

    # Simple 7% sales tax
    TAX_RATE = 0.07
    tax_amount = subtotal * TAX_RATE
    final_total = subtotal + tax_amount

    print("\n" + "#"*50)
    print("           ORDER SUMMARY")
    print("#"*50)
    print(f"Subtotal: {'':<34} {subtotal:.2f}")
    print(f"Tax (7.0%): {'':<32} {tax_amount:.2f}")
    print("-" * 50)
    print(f"TOTAL AMOUNT DUE: {'':<23} {final_total:.2f}")
    print("#"*50)

    # Prompt for confirmation
    confirm = input("Confirm purchase (yes/no)? ").lower()
    if confirm == 'yes':
        print("\n Thank you for your order! Your payment has been processed.")
        global shopping_cart
        shopping_cart = {} # Clear the cart after purchase
    else:
        print("\nOrder canceled. You have returned to the main menu.")


def main_menu():
    """Displays the main menu options."""
    print("\n" + "*"*40)
    print("       Welcome to the Tech Shop CLI")
    print("*"*40)
    print("1. View Products")
    print("2. Add Item to Cart")
    print("3. View Shopping Cart")
    print("4. Checkout")
    print("5. Exit")
    print("*"*40)

def main():
    """The main application loop."""
    while True:
        main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            print("\n Thank you for using the Tech Shop App. Goodbye!")
            sys.exit(0)
        else:
            print("\n Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the script
if __name__ == "__main__":
    main()