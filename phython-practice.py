num1=int(input("Enter the number:"))
operator=input("Enter the operator(+,-,*,/)")
num2=int(input("Enter the number:"))

if operator == "+":
    result=num1+num2
    print("result:",result)
elif operator == "-":
    result=abs(num1-num2)
    print("REsult:",result)
elif operator == "*":
    result=num1*num2
    print("Result:",result) 
elif operator == "/":
   
    if num2!=0:
        result=num1/num2    
        print("num1/num2 is divisble")
        print("Result:",result)
    else:
        print("It is not divisible")
    
else:
    print("It is not a operator")              
       
    
