#DSC510
#Assignment5.1
#Dominick Taylor
#1/15/2021
#This program uses loops and fuctions to perform calculations


def performCalculation():
    while True:
        operation = input("Please enter your desired math operation: add, sub, multi, div -")
        num1 = float(input("Please enter your first number"))
        num2 = float(input("Please enter your second number"))

        if operation == 'add':
            answer = num1 + num2
            print("You answer is ", answer)
            rerun = input("Enter y to perform another operation.\nEnter n to close")
            if rerun == 'y':
                continue
            else:
                break
        elif operation == 'sub':
            answer = num1 - num2
            print("You answer is ", answer)
            rerun = input("Enter y to perform another operation.\nEnter n to close")
            if rerun == 'y':
                continue
            else:
                break
        elif operation == 'multi':
            answer = num1 * num2
            print("You answer is ", answer)
            rerun = input("Enter y to perform another operation.\nEnter n to close")
            if rerun == 'y':
                continue
            else:
                break
        elif operation == 'div':
            answer = num1 / num2
            print("You answer is ", answer)
            rerun = input("Enter y to perform another operation.\nEnter n to close")
            if rerun == 'y':
                continue
            else:
                break


def calculateAverage():
    total = 0
    runval = int(input("How many values will you need to calculate the average of ?"))
    for x in range(0, runval):
        number = int(input("please enter a number"))
        total = total + number
    avg = round(total / runval, 2)
    print("The total of the values you entered is " ,total)
    print("The average of the values you entered in ", avg)


while True:
    welcome = input(print("Welcome user!\nTo perform a math operation enter 1. \nTo Calculate an average enter 2.\nTo close enter d. \n"))
    if welcome == '1':
        performCalculation()
    elif welcome == '2':
        calculateAverage()
    elif welcome == "d":
        break
