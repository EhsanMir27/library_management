import logging
from datetime import datetime
logging.basicConfig(filename='file.log',level=40)
logger=logging.getLogger()
def calculate_expenses():
    all_expenses = {}
    total_expense = 0
    while True:
        user_choice = input(f'1.add\n2.show all\n3.total\n4.khorouj\n->')
        if user_choice == '1':
            try:
                expenses_title = input(f'enter expense title : ')
                expenses=int(input(f'add expense : '))
            except ValueError as v:
                logger.log(msg=f'({datetime.now()}){v}', level=40)
                print('wrong input ')
            print('-'*30)
            all_expenses[expenses_title]=expenses
            total_expense= total_expense + expenses
        elif user_choice == '2':
            print(all_expenses)
            print('-' * 30)
        elif user_choice == '3':
            print(all_expenses)
            print(total_expense)
            print('-' * 30)
        else :
            exit()
calculate_expenses()





