#DSC510
#Assignment4.1
#Dominick Taylor
#1/08/2021
#Calculate the price of fiber optic cable with discounts using a function

#Print Welcome Message
messege = '****Welcome to your neighborhood Fiber Optic Supplier*****'
print(messege)

#retrieve the user's company name
usercompany= input('Please enter your company name and press enter ')
print('Thank you ', usercompany,' for shopping with us')
print("\n")

#Calculate Cable cost function
def cableCal (feet = float(input(" Please enter your desired cable length in feet")), price = .87):
    if feet >= 500:
        totalcost = feet * (price -.37 )
    elif feet >= 250 and feet < 500:
        totalcost = feet * (price - .17)
    elif feet >= 100 and feet < 250:
        totalcost = feet * (price - .07)
    else:
        totalcost = feet * price
    print(" Thank you" , usercompany , "for shopping with us your total cost is $",round(totalcost,2) )

print("\n")
print('**********************************')
cableCal()



