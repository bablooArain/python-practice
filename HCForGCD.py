num1 = int(input("Enter first second number: "))
num2 = int(input("Enter second number: "))
if(num1 >= num2):
    divisor = num1 -1 
else:
    divisor = num2 -1    
while(1):
    if(num1 % divisor == 0 and num2 % divisor == 0):
        print("The GCD is: ",divisor)
        break
    divisor -= 1
    if(divisor == 1):
        break