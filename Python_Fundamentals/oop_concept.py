class BankAccount:
    
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            
    def display_balance(self):
        print(f"Account Owner: {self.owner} | Current Balance: ${self.balance:.2f}")

if __name__ == "__main__":
    my_account = BankAccount("Alice", 100.0)
    print("--- Account Activity ---")
    my_account.display_balance()
    my_account.deposit(50.0)
    my_account.withdraw(25.0)
    my_account.withdraw(500.0)
    
    print("\nOOP script executed successfully. Ready to commit and push!")