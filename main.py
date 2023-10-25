#class Dog():
#Класс собака
#    def __init__(self, name):
#        self.name = name
#
#    def say_hi(self):
#        print("Я @ Ты @")
#    
import datetime
from os import system

class Transaction():
    #Класс транзакция
    def __init__(self, type="", date="", summ="", category="", comment="") -> None:
        self.type = type
        self.date = date
        self.summ = summ
        self.category = category
        self.comment = comment
        pass

    def out(self, counter=0):
        if counter == 0:
            print(f"Транзакция с типом {self.type}, с дата = {self.date}, сумма = {self.summ}, категория — {self.category}, комментарий: {self.comment}")
        else:
            print(f"{counter}. Транзакция с типом {self.type}, с дата = {self.date}, сумма = {self.summ}, категория — {self.category}, комментарий: {self.comment}")

class Controller():
    #Контроллер консоли пользователя
    def __init__(self) -> None:
        self.transactions = []
        pass
    def intro(self):
        print(f"Привет!\nЭто приложение для фиксирования трат.")
        input()

    def add(self):
        print("Введи тип транзакции: ")
        type_of_transactions = input()
        print("Транзакция за сегодня? (y/n)")
        result = input()
        if result == 'y':
            date = datetime.date.today().strftime('%d.%m.%y')
        else: 
            print("Введи дату: ")
            date = input()
        print("Введи сумму: ")
        summ = input()
        print("Введи категорию: ")
        category = input()
        print("Введи комментарий: ")
        comment = input()
        self.transactions.append(Transaction(type_of_transactions,date,summ,category,comment))
    def get(self,flag=True):
        if len(self.transactions) == 0: 
            print("Ты ещё не записал транзакции...")
            input()
            return
        if flag:
            for transaction in self.transactions:
                transaction.out()
            input()
        else:
            for transaction in self.transactions:
                if transaction.date == datetime.date.today().strftime('%d.%m.%y'):
                    transaction.out()
            input()
    
    def del_one(self):
        if len(self.transactions) == 0:
            print("Ты ещё не записал транзакции...")
            input()
            return
        print("Какую транзакцию удалить?")
        counter = 1
        for transaction in self.transactions:
           transaction.out(counter)
           counter+=1
        result = int(input())
        if result > len(self.transactions):
            print("Нет такой транзакции...")
            input()
            return
        del_trans = self.transactions.pop(int(result)-1)
        print(f"Транзакция\n{del_trans.out()} удалена!")

    def listen(self):
        self.intro()
        while True:
            system('cls||clear')
            print(f"Что сделать:\n1. Записать транзакцию.\n2. Получить все транзакции\n3. Получить все транзакции за сегодня\n4. Удалить транзакцию")
            result = input()
            match result:    
                case "1":
                    self.add()
                case "2":
                    self.get()
                case "3":
                    self.get(False)
                case "4":
                    self.del_one()
                case _:
                    print("Я тебя не понимаю, попробуй ещё раз...")

c = Controller()
c.listen()