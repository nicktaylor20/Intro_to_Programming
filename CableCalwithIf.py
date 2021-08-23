#DSC510
#Assignment3.1
#Dominick Taylor
#12/14/2020
#Calculate the price of fiber optic cable with discounts

#Print Welcome Message
messege = '****Welcome to your neighborhood Fiber Optic Supplier*****'
print(messege)

#retrieve the user's company name
usercompany= input('Please enter your company name and press enter ')
print('Thank you ', usercompany,' for shopping with us')

#Gather the required amount of cable
cablelength = float(input('Please enter your desired cable length in feet '))
print('You entered', cablelength, 'ft')

#Calculate Cable cost
if cablelength >= 500:
    cablecost = round(cablelength * 0.50, 2)
    print('You requested over 500 ft of cable. You qualify for our Gold discount price of $0.50')
elif cablelength >= 250 and cablelength < 500:
    cablecost = round(cablelength * 0.70, 2)
    print('You requested over 250 ft of cable. You qualify for our Silver discount price of $0.70')

elif cablelength >= 100 and cablelength < 250:
    cablecost = round(cablelength * 0.80, 2)
    print('You requested over 100 ft of cable. You qualify for our Bronze discount price of $0.80')
else:
    cablecost = round(cablelength * 0.87, 2)

print('*********************************************')
#print statement for total cost
print(" Thank you ", usercompany, "for shopping with us !")
print(" Total feet of cable requested: ", cablelength)
print(" your total cost is: $ ", cablecost)