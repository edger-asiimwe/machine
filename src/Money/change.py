
def moneyUserInput(glMoney):

    quarters_count = 0

    cash_put = 0
    strValueCent = 0
    gCents = round(glMoney * 100)
    while cash_put < gCents:
        print(f'Payment due:  dollars and  cents')
        money = input('Indicate your deposit: ')
        if money == 'n':
            strValueCent = 5
        elif money == 'd':
            strValueCent = 1
        elif money == 'q':
            strValueCent = 25
        elif money == 'o':
            strValueCent = 100
        elif money == 'f':
            strValueCent = 500
        elif money == 'c':
            break
        else:
            pass

        cash_put = cash_put + strValueCent

    if cash_put == gCents:
        print('No change due!!')
    else:
        balance = cash_put - gCents

        quarters = balance // 25
        print(quarters)
        quarters_count = quarters
        print(quarters_count)
        

        

moneyUserInput(2.50)

        









