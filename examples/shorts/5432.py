# /tmp/test/transaction.py
class Transaction:
    def __init__(self, initial_amount: float):
        self.balance = initial_amount

    def process_payment(self, amount: float):
        # Trying to reference local variable balance without initializing
        if self.balance >= amount:
            self.balance -= amount
            print(f"Payment of ${amount:.2f} processed. Remaining balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")

    def refund(self, amount: float):
        # Correctly using instance variable with self keyword
        self.balance += amount
        print(f"Refund of ${amount:.2f} processed. New balance: ${self.balance:.2f}")

# /tmp/test/main.py
from /tmp/test/transaction import Transaction

# Create an instance of Transaction
transaction = Transaction(initial_amount=100.0)

# Process a payment
transaction.process_payment(50.0)

# Process a refund
transaction.refund(20.0)

# Process a payment that would cause UnboundLocalError if self is missed
transaction.process_payment(80.0)

# This code demonstrates how missing the 'self' keyword can lead to an UnboundLocalError in class methods.
