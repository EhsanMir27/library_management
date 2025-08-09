expenses=0
all_expenses=[]
continue_='yes'
while continue_=='yes':
    user_choice=str(input('enter your choice :\n'
                          '1.add expenses\n'
                          '2.show all expenses\n'
                          '3.show total expenses\n'
                          '4.khorouj\n->'))
    if user_choice in ['add expenses','show all expenses','show total expenses','khorouj']:
        pass
    else :
        print('wrong input')
        user_choice = str(input('enter your choice :\n'
                                '1.add expenses\n'
                                '2.show all expenses\n'
                                '3.show total expenses\n'
                                '4.khorouj\n->'))
    if user_choice=='add expenses':
        expense_title=str(input('enter expense title :'))
        expenses_amount=int(input('enter expense amount :'))
        all_expenses.append((expense_title,expenses_amount))
        expenses=expenses+expenses_amount



    if user_choice=='show all expenses':
        print(f'all expenses title are : {all_expenses}\n-------------------------------')
    if user_choice=='show total expenses':
        print(f'total expenses : {expenses}\n-------------------------------')
    if user_choice=='khorouj':
        break
print('-------------------------------\nyou exited from the app')