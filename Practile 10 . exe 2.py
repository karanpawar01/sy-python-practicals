products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

search_item = input("Enter the product name to search: ")

found = False

for i in range(len(products)):
    if products[i].lower() == search_item.lower():
        print(f"{search_item} is available at index {i}.")
        found = True
        break

if not found:
    print(f"{search_item} is not available in the inventory.")
