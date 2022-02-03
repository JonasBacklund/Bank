class Account:
    def __init__(self, accNumber, accType, balance):
        self.balance = float(balance)
        self.accType = accType
        self.accNumber = accNumber