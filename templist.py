#DSC510
#Assignment6.1
#Dominick Taylor
#1/22/2021
#This program will allow users to enter temps and using list, report back information


temperature = []
while True:
    inp = input(" Please enter a temperatures. Type done when finished. ")
    if inp == 'done':
        break
    values = int(inp)
    temperature.append(values)

print("The largest temperature you entered was: ", max(temperature))
print("The smallest temperature you entered was ", min(temperature))
print("You entered ", len(temperature), "temperatures")
