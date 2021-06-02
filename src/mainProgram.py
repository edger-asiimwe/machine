#Global variables of stock coins
nickels, dimes, quarters, one_dollar, five_dollar = 25, 25, 25, 0, 0

'''Global variables of money in xx.xx and cents ie xx.xx * 100 to enable us call them by other functions
They are also updated by another function'''
g_money_toPay, g_cents_toPayConverted = 0, 0

'''Global variables of the coins inserted by the user, These will be updated by automatically after every user
We use a global keyword to update it inside another function, Since a function cant directly change a global variable'''
g_nickles_count, g_dimes_count, g_quarters_count, g_ones_count, g_five_count = 0, 0, 0, 0, 0

def menu_message():
    '''Print Menu function'''
    print('MENU FOR DEPOSITS')
    print('n -- deposit a nickel')
    print('d -- deposit a dime')
    print('q -- deposit a quarter')
    print('o -- deposit a one dollar bill')
    print('f -- deposit a five dollar bill')
    print('c -- caancel the deposit')

def stock_contains(n_value, d_value, q_value, o_value, f_value):
    '''Function prints the current stock value, Receives global variables of the coin stock as arguments
        n_value will be having a value of the global stock and print it'''
    print(f'{n_value:>2} -- nickels')  
    print(f'{d_value:>2} -- dimes')
    print(f'{q_value:>2} -- quarter')
    print(f'{o_value:>2} -- one dollar bill')
    print(f'{f_value:>2} -- five dollar bill')

def testUserInput():
    '''testUserInput function processes the value of the item, This function doesnt receive any value but returns some to the caller'''
    money = input("Enter the purchase price (xx.xx) or `q' to quit: ") #prompt the user for the money of the item/to be paid
    status = ''
    if money == 'q':
        status, moneyToPay, totalCents = 'quit', 0, 0
    else:
        moneyToPay = float(money)
        totalCents = round(moneyToPay * 100) #full cents contained in the moneyToPay variable
        #the totalCenyts are tested to see if the satisfy the condition
        #We use cents as whole numbers because it would be hard to implement it using a float type
        if(totalCents % 5) == 0 and totalCents >= 0:
            status = 'YES' #sets status to YES if it satisfies the condition
        else:
            status = 'NO' #And no if it doesnt
    return status, moneyToPay, totalCents #Returns the status, moneytoPay as xx.xx and totalCents as a whole number
    
def updateStock(upDate_nickles, upDate_dimes, upDate_quarters, upDate_oneDollar, upDate_fiveDollar):
    '''updateStock function updates the domination stock, This function will be called after the machine has given out the balance
        Afterwards, it will update the stock so that the next user views the stock thats actually available'''
    global nickels, dimes, quarters, one_dollar, five_dollar
    
    nickels = nickels + upDate_nickles
    dimes = dimes + upDate_dimes
    quarters = quarters + upDate_quarters
    one_dollar = one_dollar + upDate_oneDollar
    five_dollar = five_dollar + upDate_fiveDollar

def deductStock(upDate_nickles, upDate_dimes, upDate_quarters):
    '''This function updates the coin stock after the user has got his or her change'''
    global nickels, dimes, quarters
    
    nickels = nickels - upDate_nickles
    dimes = dimes - upDate_dimes
    quarters = quarters - upDate_quarters
    
def moneyUserInput(value_toBePaid):
    '''Function to determine the balance. Receives a value (value_toBePaid which is cents)
        Using global so that we can be able to change the global coin counter'''
    global g_nickles_count, g_dimes_count, g_quarters_count, g_ones_count, g_five_count
    
    #counter for coins put (denominations)
    nickles_count, dimes_count, quarters_count, ones_count, five_count = 0, 0, 0, 0, 0

    cash_put = 0 #money put by the user
    strValueCent = 0 #stores a value of either a dime etc to be processed
    bal = round(value_toBePaid)
    while cash_put < value_toBePaid:
        print(f'Payment due: {bal//100} dollars and {bal%100} cents')
        money = input('Indicate your deposit: ')
        if money == 'n':
            strValueCent = 5 
            nickles_count += 1 #increments the coin counter for the denomination, this applies for the other denominations
        elif money == 'd':
            strValueCent = 10
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

        bal = bal - strValueCent   
        cash_put = cash_put + strValueCent #increments the cash put after every round of user input

    #Assigning the global variables new values
    g_nickles_count = nickles_count
    g_dimes_count = dimes_count
    g_quarters_count = quarters_count
    g_ones_count = ones_count
    g_five_count = five_count
    
    return cash_put - value_toBePaid

def changeMaker(balToGive):
    '''This determines the coins change to be given out depending on the limits'''
    quartersTo, balToDimes = divmod(balToGive, 25)
    if quartersTo > quarters:
        flag = quartersTo - quarters
        quartersTo = quarters
        balToDimes = balToDimes + flag * 25
    else:
        balToDimes = balToDimes
        
    dimesTo, balToNickles = divmod(balToDimes, 10)
    if dimesTo > dimes:
        flag = dimesTo - dimes
        dimesTo = dimes
        balToNickles = balToNickles + flag * 10
    else:
        balToNickles = balToNickles

    nicklesTo, balToManager = divmod(balToNickles, 5)
    if nicklesTo > nickels:
        flag = nicklesTo - nickels
        nicklesTo = nickels
        balToManager = balToManager + flag * 5
    else:
        balToManager = balToManager

    return quartersTo, dimesTo, nicklesTo, balToManager

def printReceipt(n_tip, d_tip, q_tip):
    '''This prints the receipt plus the coins to give out'''
    print('Please take the change below!!')
    if q_tip > 0:
        print(f'{q_tip} -- Quarters')
    if d_tip > 0:
        print(f'{d_tip} -- Dimes')
    if n_tip > 0:
        print(f'{n_tip} -- Nickles')
    
def main():
    while True:
        print('WELCOME TO THE COIN CHANGE MAKER MACHINE!!!\nStock contains!!!')
        #We call testUserInput, it returns the values which include a YES or NO and the money
        stock_contains(nickels, dimes, quarters, one_dollar, five_dollar)
        inStatus, money_toPay, total_ofCents = testUserInput() 

        #Refrence global variables
        global g_cents_toPayConverted, g_money_toPay 
        
        if inStatus == 'quit':
            print('Thanks for trying our servive, hope to see you soon!!\n')
            pass
        else:
            if inStatus == 'YES': #inStatus contains a YES or NO showing that the money is valid
                
                #We assign values to the global variables listed below
                #This is to enable us the values anywhere in any other function in the program without calling the function which gave us those values again
                g_money_toPay = money_toPay
                g_cents_toPayConverted = total_ofCents

                menu_message() #Call of menu_message which we defined
                balance_toGive = moneyUserInput(total_ofCents) #Call of this function returns the balance which we store in balance_toGive
                #We shall use this value to pass it to the coin dispenser function
                updateStock(g_nickles_count, g_dimes_count, g_quarters_count, g_ones_count, g_five_count)
                if balance_toGive == 0:
                    print('There is no change for you!!!')
                else:
                    quartersTo, dimesTo, nicklesTo, balToManager = changeMaker(balance_toGive)
                    quartersTo, dimesTo, nicklesTo, balToManager = round(quartersTo), round(dimesTo), round(nicklesTo), round(balToManager)
                    if balToManager == 0:
                        printReceipt(nicklesTo, dimesTo, quartersTo)
                    else:
                        printReceipt(nicklesTo, dimesTo, quartersTo)
                        print('\n\n')
                        print(f'Amount due is: {balToManager // 100} dollars and {balToManager & 100} cents')
                    deductStock(nicklesTo, dimesTo, quartersTo)
            else:
                print('Illegal price, Must be a non-negative multiple of 5 cents.\n')
        
main()