nickels = 25
dimes = 25
quarters = 25
one_dollar = 0
five_dollar = 0

gMoney = 0

def menu_message():
    print('MENU FOR DEPOSITS')
    print('n -- deposit a nickel')
    print('d -- deposit a dime')
    print('q -- deposit a quarter')
    print('o -- deposit a one dollar bill')
    print('f -- deposit a five dollar bill')
    print('c -- caancel the deposit')

def stock_contains(n_value, d_value, q_value, o_value, f_value):
    print(f'{n_value} nickels')
    print(f'{d_value} dimes')
    print(f'{q_value} quarter')
    print(f'{o_value} one dollar bills')
    print(f'{f_value} five dollar bills')
   
def testUserInput():
    moneyToPay = float(input("Enter the purchase price (xx.xx) or `q' to quit: "))
    global gMoney
    gMoney = moneyToPay
    status = ''
    dollar = moneyToPay // 1
    cents = round((moneyToPay % 1), 2)
    centsToFull_digit = cents * 100
    totalCents = (dollar * 100) + round(centsToFull_digit)
    if(totalCents % 5) == 0 and totalCents >= 0:
        status = 'YES'
    else:
        status = 'NO'
    return status, 

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

def moneyUserInput(gMoney):
    cash_put = 0
    strValueCent = 0
    while cash_put <= gMoney:
        print(f'Payment due:  dollars and  cents')
        money = input('Indicate your deposit: ')
        if money == 'n':
            strValueCent = 0.05
        elif money == 'd':
            strValueCent = 0.1
        elif money == 'q':
            strValueCent = 0.25
        elif money == 'c':
            break
        else:
            pass

        cash_put = cash_put + strValueCent


while True:
    if testUserInput() == 'YES':
        menu_message()
        
    else:
        print('Illegal price: Must be a non-negative multiple of 5 cents.\n')
        





#Does not check whether its a negative or positive



