class Customer:
    def __init__(self, cID, name, ssn):
        self.cID = cID
        self.name = name
        self.ssn = ssn
        self.accounts = []