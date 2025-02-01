'''https://prepare.sh/interview/devops/674e5d3af0f2c7445d2ccfb0'''

class BankAccount:
    
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount: float) -> str:
        if(amount <= 0):
            raise ValueError(f"Error: Deposit amount {amount} must be greater than 0. A positive value")
        self.balance += amount
        return f"Deposit successful. New balance is {self.balance}"
            
    def withdraw(self, amount: float) -> str:
        if(amount <= 0):
            raise ValueError(f"Error: Deposit amount {amount} must be greater than 0. A positive value") 
        elif(amount > 0 and amount <= self.balance):
            self.balance -= amount
            return f"Withdrawn {amount}. Remaining balance is {self.balance}"
        else:
            raise ValueError(f"Error: Insufficient balance. Current balance is {self.balance}, Requested amount: {amount}")
    
    def get_balance(self) -> float:
        if(self.balance > 0):
            return self.balance
        
def main():
    account = BankAccount("Sozhan", 1000.0)
    
    # Test deposit functionality
    print(account.deposit(500.0))  # Expected: Deposit successful. New balance is 1500.0

    # Test withdrawal functionality
    print(account.withdraw(200.0))  # Expected: Withdrawn 200.0. Remaining balance is 1300.0


    # print(account.deposit(-100.0)) # this will throw error
    
    # Test invalid deposit (negative amount)
    try:
        print(account.deposit(-100.0))
    except ValueError as e:
        print(e)  # Expected: Error: Deposit amount must be positive. Provided: -100.0

    # Test invalid withdrawal (negative amount)
    try:
        print(account.withdraw(-50.0))
    except ValueError as e:
        print(e)  # Expected: Error: Withdrawal amount must be positive. Provided: -50.0

    # Test insufficient balance
    try:
        print(account.withdraw(2000.0))
    except ValueError as e:
        print(e)  # Expected: Error: Insufficient balance. Available: 1300.0, Requested: 2000.0

    # Test get_balance functionality
    print(f"Available balance: {account.get_balance()}")  # Expected: Available balance: 1300.0
    
if __name__ == "__main__":
    main()