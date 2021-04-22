#stock
nickels = 25
dimes = 25
quarters = 25
one_dollar = 0
five_dollar = 0
#stock

g_money_toPay = 0
g_cents_toPayConverted = 0

#denminations counter global
g_nickles_count = 0
g_dimes_count = 0
g_quarters_count = 0
g_ones_count = 0
g_five_count = 0 
#denminations counter global

def menu_message():
    print('MENU FOR DEPOSITS')
    print('n -- deposit a nickel')
    print('d -- deposit a dime')
    print('q -- deposit a quarter')
    print('o -- deposit a one dollar bill')
    print('f -- deposit a five dollar bill')
    print('c -- caancel the deposit')

def stock_contains(n_value, d_value, q_value, o_value, f_value):
    print(f'{n_value} -- nickels')
    print(f'{d_value} -- dimes')
    print(f'{q_value} -- quarter')
    print(f'{o_value} -- one dollar bill')
    print(f'{f_value} -- five dollar bill')
   
def testUserInput():
    moneyToPay = float(input("Enter the purchase price (xx.xx) or `q' to quit: "))
    status = ''
    dollar = moneyToPay // 1
    cents = moneyToPay % 1
    finalCents = round(cents,2)
    centsToFull_digit = finalCents * 100
    totalCents = (dollar * 100) + round(centsToFull_digit)
    if(totalCents % 5) == 0 and totalCents >= 0:
        status = 'YES'
    else:
        status = 'NO'
    return status, moneyToPay, totalCents

def updateStock(upDate_nickles, upDate_dimes, upDate_quarters, upDate_oneDollar, upDate_fiveDollar):
    global nickels
    global dimes
    global quarters
    global one_dollar
    global five_dollar

    nickels = nickels + upDate_nickles
    dimes = dimes + upDate_dimes
    quarters = quarters + upDate_quarters
    one_dollar = one_dollar + upDate_oneDollar
    five_dollar = five_dollar + upDate_fiveDollar

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

def main():
    while True:
        inStatus, money_toPay, total_ofCents = testUserInput()
        global g_cents_toPayConverted 
        global g_money_toPay 
        
        if inStatus == 'YES':
            g_money_toPay = money_toPay
            g_cents_toPayConverted = total_ofCents

            menu_message()
            balance_toGive = moneyUserInput(total_ofCents)
            print(balance_toGive)
        else:
            print('Illegal price, Must be a non-negative multiple of 5 cents.\n')
        
main()