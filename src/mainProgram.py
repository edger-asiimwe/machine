#Global variables of stock coins
nickels = 25
dimes = 25
quarters = 25
one_dollar = 0
five_dollar = 0


#Global variables of money in xx.xx and cents ie xx.xx * 100 to enable us call them by other functions
#They are also updated by another function
g_money_toPay = 0
g_cents_toPayConverted = 0


#Global variables of the coins inserted by the user
#These will be updated by automatically after every user
#We use a global keyword to update it inside another function
#Since a function cant directly change a global variable
g_nickles_count = 0
g_dimes_count = 0
g_quarters_count = 0
g_ones_count = 0
g_five_count = 0 


#Print Menu function
def menu_message():
    print('MENU FOR DEPOSITS')
    print('n -- deposit a nickel')
    print('d -- deposit a dime')
    print('q -- deposit a quarter')
    print('o -- deposit a one dollar bill')
    print('f -- deposit a five dollar bill')
    print('c -- caancel the deposit')


#Function prints the current stock value
#Receives global variables of the coin stock as arguments
def stock_contains(n_value, d_value, q_value, o_value, f_value):
    #n_value will be having a value of the global stock and print it
    print(f'{n_value:>2} -- nickels')  
    print(f'{d_value:>2} -- dimes')
    print(f'{q_value:>2} -- quarter')
    print(f'{o_value:>2} -- one dollar bill')
    print(f'{f_value:>2} -- five dollar bill')


#testUserInput function processes the value of the item
#This function doesnt receive any value but returns some to the caller
def testUserInput():
    moneyToPay = float(input("Enter the purchase price (xx.xx) or `q' to quit: ")) #prompt the user for the money of the item/to be paid
    status = ''
    dollar = moneyToPay // 1 
    cents = moneyToPay % 1
    finalCents = round(cents,2)
    centsToFull_digit = finalCents * 100
    totalCents = (dollar * 100) + round(centsToFull_digit) #full cents contained in the moneyToPay variable
    #the totalCenyts are tested to see if the satisfy the condition
    #We use cents as whole numbers because it would be hard to implement it using a float type
    if(totalCents % 5) == 0 and totalCents >= 0:
        status = 'YES' #sets status to YES if it satisfies the condition
    else:
        status = 'NO' #And no if it doesnt
    return status, moneyToPay, totalCents #Returns the status, moneytoPay as xx.xx and totalCents as a whole number
    

#updateStock function updates the domination stock
#This function will be called after the machine has given out the balance
#Afterwards, it will update the stock so that the next user views the stock thats actually available
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


#Function to determine the balance
#Receives a value (value_toBePaid which is cents)
def moneyUserInput(value_toBePaid):
    #Using global so that we can be able to change the global coin counter
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

    cash_put = 0 #money put by the user
    strValueCent = 0 #stores a value of either a dime etc to be processed
    while cash_put < value_toBePaid:
        print(f'Payment due:  dollars and  cents')
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

        cash_put = cash_put + strValueCent #increments the cash put after every round of user input

    #Assigning the global variables new values
    g_nickles_count = nickles_count
    g_dimes_count = dimes_count
    g_quarters_count = quarters_count
    g_ones_count = ones_count
    g_five_count = five_count
    
    balance = cash_put - value_toBePaid 
    return balance


def main():
    print('WELCOME TO THE COIN CHANGE MAKER MACHINE')
    while True:
        #We call testUserInput, it returns the values which include a YES or NO and the money
        inStatus, money_toPay, total_ofCents = testUserInput() 

        #Refrence global variables
        global g_cents_toPayConverted 
        global g_money_toPay 
        
        if inStatus == 'YES': #inStatus contains a YES or NO showing that the money is valid
            
            #We assign values to the global variables listed below
            #This is to enable us the values anywhere in any other function in the program without calling the function which gave us those values again
            g_money_toPay = money_toPay
            g_cents_toPayConverted = total_ofCents

            menu_message() #Call of menu_message which we defined
            balance_toGive = moneyUserInput(total_ofCents) #Call of this function returns the balance which we store in balance_toGive
            #We shall use this value to pass it to the coin dispenser function
            print(balance_toGive)
        else:
            print('Illegal price, Must be a non-negative multiple of 5 cents.\n')
        

main()