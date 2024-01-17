def main():
    class CustomerInfo:
        def __init__(self):
            self.name = ""
            self.phnum = ""
            self.id = 0
            self.tpoint = 0

    def show_customer_info(obj, n):
        id = int(input("\nEnter customer id: "))
        for i in range(n):
            if id == obj[i].id:
                print("\nCustomer name:", obj[i].name)
                print("Customer phone number:", obj[i].phnum)
                print("Customer total points:", obj[i].tpoint)
                print("Rewards available:", obj[i].tpoint // 10)
                return
        print("Customer not found. Please enter a valid customer id.")

    def display_top_customers(obj, n):
        print("\nTop Customers:")
        obj.sort(key=lambda x: x.tpoint, reverse=True)
        for i in range(min(5, n)):
            print("Name:", obj[i].name)
            print("Total Points:", obj[i].tpoint)
            print()

    def redeem_points(obj, n):
        id = int(input("\nEnter customer id: "))
        for i in range(n):
            if id == obj[i].id:
                points = obj[i].tpoint
                if points >= 10:
                    rewards = points // 10
                    print("\nCustomer:", obj[i].name)
                    print("Available Points:", points)
                    print("Rewards to be redeemed:", rewards)
                    print("Congratulations! You can choose from the following rewards:")
                    print("1. Discount Coupon (10% off)")
                    print("2. Gift Card (worth $10)")
                    print("3. Free Movie Ticket")
                    choice = int(input("Enter your choice (1-3): "))
                    if choice == 1:
                        print("You have redeemed a 10% discount coupon!")
                    elif choice == 2:
                        print("You have redeemed a $10 gift card!")
                    elif choice == 3:
                        print("You have redeemed a free movie ticket!")
                    else:
                        print("Invalid choice. No rewards redeemed.")
                else:
                    print("Insufficient points to redeem rewards.")
                return
        print("Customer not found. Please enter a valid customer id.")

    def calculate_points():
        try:
            purchase_amount = float(input("\nEnter the purchase amount: "))
            points = int(purchase_amount / 10)
            print("Earned Points:", points)
            print("Calculation: $10 spent = 1 point")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if __name__ == "__main__":
        obj = []
        n = int(input("\nEnter number of customers: "))
        print("Enter customer information!")

        def get_valid_name():
            while True:
                name = input("Enter customer name: ")
                if name.isalpha():
                    return name
                print("Invalid input. Please enter alphabetic characters only.")

        def get_valid_phnum():
            while True:
                phnum = input("Enter customer phnum: ")
                if phnum.isdigit() and len(phnum) == 10:
                    return phnum
                print("Invalid input. Please enter a 10-digit numeric phone number.")

        def get_valid_id():
            while True:
                try:
                    id = int(input("Enter customer id: "))
                    # Check uniqueness of ID
                    if any(cust.id == id for cust in obj):
                        print("ID already exists. Please enter a unique ID.")
                    else:
                        return id
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        def get_valid_tpoint():
            while True:
                try:
                    tpoint = int(input("Enter customer tpoint: "))
                    return tpoint
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        for i in range(n):
            customer = CustomerInfo()
            print(f"\n{i+1} customer information:")
            customer.name = get_valid_name()
            customer.phnum = get_valid_phnum()
            customer.id = get_valid_id()
            customer.tpoint = get_valid_tpoint()
            obj.append(customer)

        while True:
            print("\nPress 1 for customer info")
            print("Press 2 to display top customers")
            print("Press 3 to redeem points for rewards")
            print("Press 4 to calculate points")
            print("Press 5 to exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                show_customer_info(obj, n)
            elif choice == 2:
                display_top_customers(obj, n)
            elif choice == 3:
                redeem_points(obj, n)
            elif choice == 4:
                calculate_points()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
