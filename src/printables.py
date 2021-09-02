class printables:
    """Class implementation for the printable items"""
    def __init__(self) -> None:
        pass

    def menu_message(self):
        """Screen print for the welcome MENU items"""
        print('MENU FOR DEPOSITS')
        print('n -- deposit a nickel')
        print('d -- deposit a dime')
        print('q -- deposit a quarter')
        print('o -- deposit a one dollar bill')
        print('f -- deposit a five dollar bill')
        print('c -- caancel the deposit')

    def stock_contains(self, n_value, d_value, q_value, o_value, f_value):
        """Function prints the current stock value, Receives global variables of the coin stock as arguments"""
        print(f'{n_value:>2} -- nickels')  
        print(f'{d_value:>2} -- dimes')
        print(f'{q_value:>2} -- quarter')
        print(f'{o_value:>2} -- one dollar bill')
        print(f'{f_value:>2} -- five dollar bill')

    def printReceipt(self, n_tip, d_tip, q_tip):
        """This prints the receipt plus the coins to give out"""
        print('Please take the change below!!')
        if q_tip > 0:
            print(f'{q_tip} -- Quarters')
        if d_tip > 0:
            print(f'{d_tip} -- Dimes')
        if n_tip > 0:
            print(f'{n_tip} -- Nickles')