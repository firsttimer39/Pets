class Account:
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance

    def enter_to_account(self, password):
        if self.password == password:
            print("Успешно!")
            print(f"Ваш текущий баланс {self.balance}")
        else:
            print("Неправильный пароль!")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесена сумма {amount}. Ваш баланс {self.balance}")
        else:
            print("Ошибка! Сумма должна быть больше нуля")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Вы не можете снять сумму превышающую ваш баланс")
        elif amount > 0:
            self.balance -= amount
            print(f"Выведена сумма {amount}. Ваш баланс {self.balance}")
        else:
            print("Ошибка! Сумма должна быть больше нуля")

    def take_money_to_send(self, amount, name_in):
        if amount > 0:
            self.balance -= amount
            print(f"Сумма {amount} будет переведена на счет пользователя {name_in} ")
        else:
            print(f'Невозможно перевести сумму равную или меньше 0')

    def get_money(self, amount, name_out):
        self.balance += amount
        print(f'Получен перевод на сумму {amount} от пользователя {name_out}')


    def show_balance(self):
        print(f'{self.name} на вашем счету {self.balance}')



John = Account("John", "12345", 1000)
Ann = Account("Ann", "56789", 1200)

#John.enter_to_account(input("Введите пароль "))
#Ann.enter_to_account(input("Введите пароль "))
#John.deposit(100)
#Ann.withdraw(-250)


John.show_balance()
Ann.show_balance()
John.take_money_to_send(200, "Ann")
Ann.get_money(200, "John")
John.show_balance()
Ann.show_balance()

