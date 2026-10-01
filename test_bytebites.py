from bytebites import Customer, MenuItem, Menu, Order

# Set up a menu
menu = Menu()
menu.add_item(MenuItem("Spicy Burger", 8.99, "Entrees", 4.7))
menu.add_item(MenuItem("Large Soda", 2.49, "Drinks", 4.2))
menu.add_item(MenuItem("Iced Tea", 2.29, "Drinks", 3.9))
menu.add_item(MenuItem("Chocolate Cake", 4.99, "Desserts", 4.8))

print("Full menu:")
for item in menu.items:
    print(f"  {item.name} - ${item.price} ({item.category}, rating {item.popularity_rating})")

print("\nDrinks only:")
for item in menu.filter_by_category("Drinks"):
    print(f"  {item.name} - ${item.price}")

# Create a customer
customer = Customer("Alex")
print(f"\nIs {customer.name} a real user before ordering? {customer.is_real_user()}")

# Place an order
order = Order(customer)
order.add_item(menu.items[0])  # Spicy Burger
order.add_item(menu.items[1])  # Large Soda
order.add_item(menu.items[3])  # Chocolate Cake

print(f"\nOrder total: ${order.get_total():.2f}")

# Record the purchase in the customer's history
customer.add_purchase(order)
print(f"Is {customer.name} a real user after ordering? {customer.is_real_user()}")
print(f"{customer.name}'s purchase history has {len(customer.purchase_history)} order(s)")
