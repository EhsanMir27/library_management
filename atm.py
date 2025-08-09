mojoudi=100000
continue_='edame'
while continue_=='edame':
    user_choice=str(input('enter you coice \n1.mojoudi\n2.variz\n3.bardasht\n4.khorouj\n->'))
    if user_choice in ['mojoudi','variz','bardasht','khorouj'] :
        pass
    else :
        print('wrong input')
        user_choice = str(input('enter you coice \n1.mojoudi\n2.variz\n3.bardasht\n4.khorouj\n->'))
    if user_choice=='mojoudi':
        print(f'your mojoudi is {mojoudi}\n-------------------------------')
    else:
        pass
    if user_choice=='variz':
        variz=int(input('enter varizi amount :'))
        mojoudi=mojoudi+variz
        print(f'your mojoudi is {mojoudi}\n-------------------------------')
    if user_choice=='bardasht':
        bardasht=int(input('enter bardashti amount :'))
        mojoudi=mojoudi-bardasht
        if mojoudi<0:
            print(f'you cant take {bardasht} from your mojoudi\ntake less')
            bardasht = int(input('enter bardashti amount :'))
        else:
            print(f'your mojoudi is {mojoudi}\n-------------------------------')

    if user_choice=='khorouj':
        break
    # continue_=str(input('edame ya khorouj ?\n->'))
    #
    # if continue_ in ['edame','khorouj']:
    #     pass
    # else:
    #     print('wrong input')
    #     continue_ = str(input('edame ya khorouj ?\n->'))
print('-------------------------------\nyou exited from the app')


