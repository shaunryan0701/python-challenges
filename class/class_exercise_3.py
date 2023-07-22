'''
Implement a class representing an account exception,
Implement a class representing a single bank account,
This class should control access to the account number and account balance attributes 
by implementing the properties:
it should be possible to read the account number only, not change it. 
In case someone tries to change the account number, raise an alarm by raising an exception;
it should not be possible to set a negative balance. 
In case someone tries to set a negative balance, raise an alarm by raising an exception;
when the bank operation (deposit or withdrawal) is above 100.000, then additional message 
should be printed on the standard output (screen) for auditing purposes;
it should not be possible to delete an account as long as the balance is not zero;
test your class behavior by:
setting the balance to 1000;
trying to set the balance to -200;
trying to set a new value for the account number;
trying to deposit 1.000.000;
trying to delete the account attribute containing a non-zero balance.
'''

class AccountException(Exception):
    pass

class BankAccount:
    def __init__(self, acc_number, balance=0.0) -> None:
        self.__account = acc_number
        self.__balance = balance

    @property
    def account(self):
        return self.__account
    
    @account.setter
    def account(self, value):
        raise AccountException("Cannot set account number")
    
    @property
    def balance(self, value):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException('Balance cannot be less than 0.00')
        else:
            self.__balance = value

    def __str__(self) -> str:
        return f'Account Number: {self.__account}, Balance {self.__balance}'

new_account = BankAccount(176661903)
print(new_account)
new_account.balance = 100

print(new_account)

try:
    new_account.balance = - 100
except AccountException as e:
    print(e)
print(new_account)
