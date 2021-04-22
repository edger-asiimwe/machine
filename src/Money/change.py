g_nickles_count = 0
g_dimes_count = 0
g_quarters_count = 0
g_ones_count = 0
g_five_count = 0 

def moneyUserInput(value_toBePaid):

    global g_nickles_count
    global g_dimes_count
    global g_quarters_count
    global g_ones_count
    global g_five_count
    
    #counter for coins put (denominations)
    nickles_count = 0
    dimes_count = 0
    quarters_count = 0
    ones_count = 0
    five_count= 0 
    #counter for coins put

    cash_put = 0
    strValueCent = 0
    while cash_put < value_toBePaid:
        print(f'Payment due:  dollars and  cents')
        money = input('Indicate your deposit: ')
        if money == 'n':
            strValueCent = 5
            nickles_count += 1
        elif money == 'd':
            strValueCent = 1
            dimes_count += 1
        elif money == 'q':
            strValueCent = 25
            quarters_count += 1
        elif money == 'o':
            strValueCent = 100
            ones_count += 1
        elif money == 'f':
            strValueCent = 500
            five_count += 1
        elif money == 'c':
            break
        else:
            pass

        cash_put = cash_put + strValueCent

    g_nickles_count = nickles_count
    g_dimes_count = dimes_count
    g_quarters_count = quarters_count
    g_ones_count = ones_count
    g_five_count = five_count
    
    balance = cash_put - value_toBePaid
    return balance


        









