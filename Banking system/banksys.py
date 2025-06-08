class Account:
    def __init__(self, acc_number, balance=0):
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_number):
        if acc_number not in self.accounts:
            self.accounts[acc_number] = Account(acc_number)
            print(f"Account {acc_number} created.")
        else:
            print("Account number already exists.")

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)
    
def main():
    bank = Bank()
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            acc_number = input("Enter new account number: ")
            bank.create_account(acc_number)
        elif choice in ('2', '3', '4'):
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == '4':
                    print(f"Account balance: ₹{account.get_balance()}")
            else:
                print("Account not found.")
        elif choice == '5':
            print("Thank You")
            print("\N{winking face}")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
