from account import Account
from customer import Customer
_path = "bank_log.txt"
customerList = []

class Bank:
    clist = []
    aID = 11111
    accNr = 1000

    def _load(self):
        r = open(_path, "r")
        for i in r.readlines():
            self.clist.append(str(i).split(":"))
        for i in range(0, len(self.clist)):
            count = 3
            length = 4
            loaded = Customer(int(self.clist[i][0]), self.clist[i][1], self.clist[i][2])
            while len(self.clist[i]) >= length:
                accountInfo = self.clist[i][count:count + 3]
                length += 3
                count += 4
                if len(accountInfo) > 1:
                    loaded.accounts.append(Account(accountInfo[0], accountInfo[1], accountInfo[2]))
            customerList.append(loaded)
        r.close()
        return self.clist

    def get_customers(self):
        for i in customerList:
            print(f"Name: {i.name}  Social Security Number: {i.ssn}")

    def add_customer(self, name, ssn):
        for customer in customerList:
            if customer.cID >= self.aID:
                self.aID += 1
            if customer.ssn == ssn:
                print("A customer with that Social Security Number already exists")
                return False
        customer = Customer(self.aID, name, ssn)
        customerList.append(customer)
        self.update()
        return True

    def update(self):
        r = open(_path, "r+")
        r.truncate(0)
        for customer in customerList:
            r.write(f"{customer.cID}:{customer.name}:{customer.ssn}:")
            for accounts in customer.accounts:
                r.write(f"{accounts.accNumber}:{accounts.accType}:{accounts.balance}:#:")
            r.write("\n")
        r.close()

    def _get_customer(self, ssn):
        for customer in customerList:
            if customer.ssn == ssn:
                return customer

    def get_customer(self, ssn):
        for customer in customerList:
            if customer.ssn == ssn:
                print(customer.cID, customer.name, customer.ssn)
                return customer
        print(f"Didn't find any customer with the Social Security Number: {ssn}")

    def change_customer_name(self, name, ssn):
        customer = self._get_customer(ssn)
        if customer.name == name and customer.ssn == ssn:
            customer.name = input("Enter your new name: ")
            self.update()

    def remove_customer(self, ssn):
        for customer in customerList:
            if customer.ssn == ssn and len(customer.accounts) == 0:
                customerList.remove(customer)
                self.update()
                break

    def add_account(self, ssn):
        for customer in customerList:
            for accounts in customer.accounts:
                if int(accounts.accNumber) >= self.accNr:
                    self.accNr += 1
        customer = self._get_customer(ssn)
        if customer.ssn == ssn:
            newAcc = Account(self.accNr, "debit", 0)
            customer.accounts.append(newAcc)
            print(newAcc.accNumber)
        self.update()

    def get_account(self, ssn, accNumber):
        customer = self._get_customer(ssn)
        for account in customer.accounts:
            if account.accNumber == accNumber:
                print(f"{account.accNumber} {account.accType} {account.balance}")
                break
            else:
                print("No customer with that accountnumber exists")

    def deposit(self, ssn, accNumber, amount):
        customer = self._get_customer(ssn)
        for account in customer.accounts:
            if int(account.accNumber) == int(accNumber):
                account.balance += int(amount)
                self.update()
                self.list_accounts(ssn)
                return True

        return False

    def withdraw(self, ssn, accNumber, amount):
        customer = self._get_customer(ssn)
        for account in customer.accounts:
            if int(account.accNumber) == int(accNumber):
                account.balance -= int(amount)
                self.update()
                return True
        return False

    def close_account(self,ssn,accNumber):
        customer = self._get_customer(ssn)
        for account in customer.accounts:
            if account.accNumber == accNumber:
                print(f"{account.accNumber} {account.accType} {account.balance}")
                customer.accounts.remove(account)
                self.update()
    def list_accounts(self,ssn):
        customer = self._get_customer(ssn)
        for account in customer.accounts:
            print(f"Account number:{account.accNumber} Account type:{account.accType} Balance:{account.balance}kr")

def menu():
    print("""What do you wish to do? 
    1. Get Customers 
    2. Add Customer 
    3. Get Customer by ssn 
    4. Change Customer username
    5. Remove Customer
    6. Add Account
    7. Get Account
    8. Deposit
    9. Withdraw
    10.List Accounts
    11.Close Account

    Enter q to quit""")
    choice = input("> ")
    if choice == "1":
        Bank().get_customers()
    elif choice == "2":
        Bank().add_customer(input("Name"), input("Social Security Number")),
    elif choice == "3":
        print(Bank().get_customer(input("Enter the Social Security Number for the customer")))
    elif choice == "4":
        Bank().change_customer_name(input("Enter old name"),input("Enter the Social Security Number for the customer"))
    elif choice == "5":
        Bank().get_customers()
        Bank().remove_customer(input("Enter the Social Security Number for the customer"))
    elif choice == "6":
        Bank().add_account(input("Enter the Social Security Number for the customer"))
    elif choice == "7":
        Bank().get_account(input("Enter the Social Security Number for the customer"), input("Enter the Account number:"))
    elif choice == "8":
        ssn = input("Enter the Social Security Number for the customer")
        Bank().list_accounts(ssn)
        Bank().deposit(ssn, input("Enter the Account number:"),float(input("amount")))
    elif choice == "9":
        ssn = input("Enter the Social Security Number for the customer")
        Bank().list_accounts(ssn)
        Bank().withdraw(ssn, input("Enter the Account number:"),float(input("amount")))
    elif choice == "10":
        Bank().list_accounts(input("Enter the Social Security qNumber for the customer"))
    elif choice == "11":
        ssn = input("Enter the Social Security Number for the customer")
        Bank().list_accounts(ssn)
        Bank().close_account(ssn,input("Enter the Account number:"))
    elif choice == "q":
        quit()
    else:
        print(f"{choice} wasn't a option")


if __name__ == '__main__':
    Bank()._load()
    while True:
        menu()

