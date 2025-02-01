# Problem Statement: Bank Account Class Implementation

## Objective:
Implement a `BankAccount` class in Python that simulates a basic bank account. The class should support deposits, withdrawals, and balance retrieval. Additionally, you should test edge cases for deposits and withdrawals to ensure the class handles all scenarios correctly.

## Requirements:

### Class Definition:
**Class Name**: `BankAccount`

### Attributes:
- `account_holder` (str): The name of the account holder.
- `balance` (float): The current balance in the account. This should be initialized to 0.0 when the account is created.

### Methods:
- `deposit(amount: float) -> None`:  
  Adds the specified amount to the account balance.  
  Raises a `ValueError` if the amount is negative or zero.

- `withdraw(amount: float) -> None`:  
  Deducts the specified amount from the account balance.  
  Raises a `ValueError` if the amount is negative, zero, or exceeds the current balance.

- `get_balance() -> float`:  
  Returns the current balance in the account.

## Edge Cases to Handle:
- Depositing a negative or zero amount.
- Withdrawing a negative or zero amount.
- Withdrawing more than the current balance.
- Depositing or withdrawing very large amounts (e.g., close to the limits of floating-point precision).

## Additional Considerations:

### Initialization:
- The `BankAccount` class should be initialized with the `account_holder` name. The balance should start at 0.0.

### Error Handling:
- Use exceptions (e.g., `ValueError`) to handle invalid operations, such as depositing or withdrawing invalid amounts.

### Precision:
- Ensure that the balance is handled as a floating-point number with appropriate precision.

### Immutability:
- The `account_holder` attribute should be immutable after initialization (i.e., it cannot be changed once the account is created).

### Documentation:
- Add docstrings to the class and its methods to describe their purpose, arguments, and return values.


Example Usage:

# Create a new bank account
```python
account = BankAccount("John Doe")
```

# Deposit money
```python
account.deposit(100.0)
print(account.get_balance())  # Output: 100.0
```

# Withdraw money
```python
account.withdraw(50.0)
print(account.get_balance())  # Output: 50.0
```

# Attempt to withdraw more than the balance
```python
try:
    account.withdraw(100.0)
except ValueError as e:
    print(e)  # Output: "Error: Insufficient balance."
```

# Attempt to deposit a negative amount
```python
try:
    account.deposit(-10.0)
except ValueError as e:
    print(e)  # Output: "Error: Deposit amount must be positive."
```

# Evaluation Criteria

## Correctness:
- The class should correctly handle deposits, withdrawals, and balance retrieval.
- It should raise appropriate exceptions for invalid operations.

## Edge Case Handling:
- The class should handle edge cases such as:
  - Negative amounts
  - Zero amounts
  - Insufficient balance

## Code Quality:
- The code should be clean, well-structured, and easy to understand.
- Use meaningful variable and method names.

## Documentation:
- The class and methods should have clear and concise docstrings.

## Robustness:
- The class should handle unexpected inputs gracefully and not crash.

# Bonus (Optional):

## Transaction History:

Extend the class to maintain a history of transactions (deposits and withdrawals) and provide a method to retrieve the transaction history.

## Interest Calculation:

Add a method to calculate and add interest to the balance based on a given annual interest rate.

## Overdraft Protection:

Add an optional overdraft limit that allows withdrawals to exceed the balance up to a specified limit.

## Multiple Accounts:

Implement a Bank class that can manage multiple BankAccount instances and provide methods to transfer funds between accounts.