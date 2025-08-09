import logging
from datetime import datetime
from logging import exception

logging.basicConfig(filename='file.log',level=40)
logger=logging.getLogger()
try:
    menu_file=open(file='menu.txt',mode='r')
except exception as e :
    logger.log(msg=f'({datetime.now()}){e}',level=40)

menu=menu_file.readlines()
menu_food={}
menu_num={}
menu_price={}
total_price=0
user_receipt={}
counter={}
for value in menu:
    num,food_name,price=value.strip().split()
    menu_food[food_name]=price
    menu_price[num]=int(price)
    menu_num[num]=food_name
if len(menu)!=0 :

    continue_='yes'
    while continue_=='yes':
        print('welcome')
        print('-'*30)
        print('menu:')
        for num, (food_name, price) in enumerate(menu_food.items(), start=1):
            print(f'{num} {food_name} {price}')

        user_order=input(f'choose your order:\n->')
        counter=int(input(f'how many ?\n->'))

        if user_order == 0:
            break
        else :
            price=menu_price[user_order]*counter
            food_name=menu_num[user_order]
            user_receipt[food_name]=price
            total_price += price
            print('-' * 30)
            print()
            print('-' * 30)
            print('user receipt:')
            for num, (food_name, price) in enumerate(user_receipt.items(), start=1):
                print(f'{counter} {food_name} {price}')
            logger.log(msg=f'({datetime.now()}) {user_receipt}',level=20)
            print(f'your total price:{total_price}')
            print('-'*30)
            continue_=input(f'want to continue : yes|no\n->')

else:
    logger.log(msg=f'({datetime.now()}) menu is empty',level=50)
    exit('empty menu')
print('thanks for your order')




