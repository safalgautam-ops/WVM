class WaterVendingMachineFSM:
    def __init__(self, water_price=40, initial_stock=10):
        self.state = "Idle"
        self.water_price = water_price  # Fixed price in cents
        self.balance = 0
        self.stock = initial_stock      # Fixed initial stock

    def insert_coin(self, amount):
        if self.stock <= 0:
            print("Machine out of water. Please come back later.")
            return

        if self.state in ["Idle", "AcceptingCoins"]:
            self.balance += amount
            self.state = "AcceptingCoins"
            print(f"Inserted {amount} cents. Current balance: {self.balance} cents.")

            if self.balance >= self.water_price:
                print("Sufficient balance reached.")
                self.state = "DispensingWater"
                self.dispense_water()
        else:
            print(f"Cannot insert coins while in '{self.state}' state.")

    def dispense_water(self):
        if self.stock <= 0:
            print("Out of stock. Cannot dispense water.")
            self.refund_balance()
            self.state = "Idle"
            return
        
        print("Dispensing clean, filtered water...")
        self.stock -= 1
        self.balance -= self.water_price

        if self.balance > 0:
            self.state = "ReturningChange"
            self.return_change()
        else:
            self.finish_transaction()

    def return_change(self):
        print(f"Returning change: {self.balance} cents.")
        self.balance = 0
        self.finish_transaction()

    def refund_balance(self):
        if self.balance > 0:
            print(f"Refunding {self.balance} cents.")
            self.balance = 0

    def cancel_transaction(self):
        if self.state == "AcceptingCoins" and self.balance > 0:
            print(f"Transaction cancelled. Refunding {self.balance} cents.")
            self.balance = 0
            self.state = "Idle"
        else:
            print("No active transaction to cancel.")

    def refill_stock(self, amount):
        if amount <= 0:
            print("Refill amount must be positive.")
            return
        self.stock += amount
        print(f"Refilled stock by {amount}. Current stock: {self.stock}")

    def show_status(self):
        print(f"State: {self.state}, Balance: {self.balance} cents, Stock: {self.stock}")

    def finish_transaction(self):
        print(f"Thank you! Please take your water. Remaining stock: {self.stock}")
        self.state = "Idle"


def admin_auth():
    ADMIN_PASSWORD = "admin123"  # Set your admin password here
    attempts = 3
    while attempts > 0:
        pw = input("Enter admin password to continue: ")
        if pw == ADMIN_PASSWORD:
            print("Admin access granted.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. Attempts left: {attempts}")
    print("Admin access denied.")
    return False


def main():
    # Fixed initial parameters (no user input)
    water_price = 40     # e.g., 40 cents per water portion
    initial_stock = 10   # e.g., 10 water portions available

    print("Welcome to the Water Vending Machine!")
    print(f"Water price is fixed at {water_price} cents.")
    print(f"Initial water stock is {initial_stock} portions.")

    machine = WaterVendingMachineFSM(water_price=water_price, initial_stock=initial_stock)

    # Main interaction loop
    while True:
        print("\nOptions:")
        print("1. Insert Coin")
        print("2. Cancel Transaction")
        print("3. Refill Stock (Admin only)")
        print("4. Show Machine Status")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            coin_input = input("Insert coin amount in cents (e.g. 10, 20, 50): ").strip()
            try:
                coin_value = int(coin_input)
                if coin_value <= 0:
                    print("Please insert a positive coin value.")
                else:
                    machine.insert_coin(coin_value)
            except ValueError:
                print("Invalid coin value entered.")
        elif choice == "2":
            machine.cancel_transaction()
        elif choice == "4":
            machine.show_status()
        elif choice == "3":
            # Admin authentication before refill
            if admin_auth():
                refill_input = input("Enter amount to refill stock: ").strip()
                try:
                    refill_value = int(refill_input)
                    machine.refill_stock(refill_value)
                except ValueError:
                    print("Invalid refill value entered.")
        elif choice == "5":
            # If a transaction is active, refund balance before exiting
            if machine.state == "AcceptingCoins" and machine.balance > 0:
                print(f"Exiting program. Refunding your balance of {machine.balance} cents.")
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()
