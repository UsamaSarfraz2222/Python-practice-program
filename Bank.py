class Bank:
    def __init__(self):
        self.balance = 0
        self.deposits = []
        self.withdrawals = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.deposits.append(amount)
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.balance:
                print("Insufficient funds. Withdrawal canceled.")
            else:
                self.balance -= amount
                self.withdrawals.append(amount)
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def print_transactions(self):
        print("\nDeposit amounts:", self.deposits)
        print("Withdrawal amounts:", self.withdrawals)


def main():
    accounts = {}  # Dictionary to store multiple bank accounts
    current_account = None

    while True:
        print("\n1. Create Account\n2. Switch Account\n3. Deposit\n4. Withdraw\n5. Check Balance\n6. Print Transactions\n7. Quit")
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        try:
            if choice == '1':
                account_name = input("Enter account name: ")
                accounts[account_name] = Bank()
                print(f"Account '{account_name}' created.")
            elif choice == '2':
                account_name = input("Enter account name: ")
                current_account = accounts[account_name]
                print(f"Switched to account '{account_name}'.")
            elif choice == '3':
                amount = float(input("Enter deposit amount: "))
                current_account.deposit(amount)
            elif choice == '4':
                amount = float(input("Enter withdrawal amount: "))
                current_account.withdraw(amount)
            elif choice == '5':
                current_account.check_balance()
            elif choice == '6':
                current_account.print_transactions()
            elif choice == '7':
                print("Exiting the bank program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except KeyError:
            print("Account not found. Please create the account first.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
