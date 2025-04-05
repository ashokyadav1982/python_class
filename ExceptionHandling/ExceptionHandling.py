class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance
    
def main():
    account = BankAccount(1000)

    try:
        print("Depositing 500...")
        account.deposit(500)
        print(f"New balance: {account.balance}")

        print("Withdrawing 200...")
        account.withdraw(200)
        print(f"New balance: {account.balance}")

        print("Withdrawing 2000...")  # This will raise an exception
        account.withdraw(2000)

        print("Withdrawing -100...")  # This will also raise an exception
        account.withdraw(-100)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()