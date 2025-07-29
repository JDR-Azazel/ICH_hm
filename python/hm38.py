"""
Создайте класс BankAccount, описывающий банковский счёт.
- Объект должен хранить имя владельца и текущий баланс.
- Реализуйте методы:
    - пополнение счёта
    - снятие средств
    - отображение баланса
- При попытке снять больше, чем есть на счёте, операция не должна выполняться.

Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.
Пример вывода:
Current balance: 150
Error: Amount must be positive.
Current balance: 150
Error: Not enough funds.
Current balance: 150
"""

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
        elif amount > self.__balance:
            print("Error: Not enough funds.")
        else:
            self.__balance -= amount

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

account = BankAccount("Alfa", 100)

account.deposit(50)
account.show_balance()

account.deposit(-10)
account.show_balance()

account.withdraw(500)
account.show_balance()

"""
Доработайте класс BankAccount.
- Каждая операция пополнения и снятия должна сохраняться в историю.
- История должна быть доступна через property history только для чтения.
История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.)

Пример вывода: 
Current balance: 50
Operation history:
Deposit: 150
Withdraw: 100
"""

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance
        self.__history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
        elif amount > self.__balance:
            print("Error: Not enough funds.")
        else:
            self.__balance -= amount
            self.__history.append(f"Withdraw: {amount}")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

    @property
    def history(self):
        return self.__history.copy()

account = BankAccount("Alfa", 0)
account.deposit(150)
account.withdraw(100)
account.show_balance()

print("Operation history:")
for operation in account.history:
    print(operation)
