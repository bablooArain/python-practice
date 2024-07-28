num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
devisor = 2
while(devisor):
    if(num1%devisor==0) and (num2%devisor==0):
        print("Here's the devisor of both: ", devisor)
        break
    elif(devisor >= num1) or (devisor >= num2):
        print("No devisor found")
        break
    devisor = devisor + 1