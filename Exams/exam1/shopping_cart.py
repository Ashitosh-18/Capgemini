def add_item(cart):
    item_name = input("Enter item name: ")
    item_price = float(input("Enter price: "))
    cart.append((item_name, item_price))  

def view_cart(cart):
    if len(cart) == 0:
        print("Your cart is empty.")
    else:
        print("Items in your cart:\n")
        for i in cart:
            print(f"Item: {i[0]}, Price: {i[1]}")
        
def cal_total(cart):
    total = 0
    for i in cart:
        total += i[1]
    return total

def main():
    cart = []  
    while True:
        print("1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total Price")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item(cart)
        elif choice == '2':
            view_cart(cart)
        elif choice == '3':
            total = cal_total(cart)
            print(f"Total price: {total}")
        elif choice == '4':
            break
        else:
            print("Enter a valid choice")

main()