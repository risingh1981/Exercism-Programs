import threading
class BankAccount:
    def __init__(self):
        self.balance = None
        self.status = None
        self.lock = threading.Lock()
                

    def get_balance(self):
        with self.lock:
            if (self.status == "Closed"):
                raise ValueError("Error: Attempting to check balance of closed account.")
            return self.balance

    def open(self):
        with self.lock:
            if (self.status == "Open"):
                raise ValueError("Error: Attempting to open an account that is already open.")
            self.status = "Open"
            self.balance = 0

    def deposit(self, amount):
        with self.lock:
            if (self.status == "Closed"):
                raise ValueError("Error: Attempting to deposit money into a closed account.")
            elif (amount <= 0):
                raise ValueError("Error: Cannot deposit zero or negative amounts.")
            self.balance += amount

        

    def withdraw(self, amount):
        with self.lock:
            if (self.status == "Closed"):
                raise ValueError("Error: Attempting to withdraw from a closed account.")
            elif (amount <= 0):
                raise ValueError("Error: Cannot withdraw 0 or negative amounts.")
            elif (amount > self.balance):
                raise ValueError("Error: Cannot withdraw more than current balance")
            self.balance -= amount

    def close(self):
        with self.lock:
            if (self.status == "Closed") or (self.status == None):
                raise ValueError("Error: Attempting to close an already closed account.")
            self.status = "Closed"
        
