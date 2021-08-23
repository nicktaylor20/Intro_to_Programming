#DSC510
#Assignment 11.1
#Dominick Taylor
#2/25/2021
#program should have a loop which allows the user to continue to add items to the cart until they request to quit.


class CashRegister :
    def __init__(self, total = 0.0, items = 0.0):
        self.total = total
        self.items = items

    def additem(self, amount):
        self.items = self.items + 1
        self.total = self.total + amount
    def gettotal(self):
        return self.total
    def getcount(self):
        return self.items



def main():
    testtrans = CashRegister(0, 0)
    while True:
        try:
            price = float(input("Please enter the price of you item(s). Enter -1 to quit "))
            if price > 0:
                testtrans.additem(price)
            elif price < -1:
                print("Please enter a valid value. Enter the price of your item or -1 to quit")
        except ValueError:
            print('Please enter a valid value. Enter the price of your item or -1 to quit ')
        finally:
            if price == -1:
                print("Your total cost is :$", round(testtrans.gettotal(), 2))
                print("Your total items purchased : ",testtrans.getcount())
                break



main()











