#python calculator
operator =input("Enter the operator(+ , -, /, * ): ")
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
if operator == "+":
    result=num1+num2
    print(result)
elif operator == "-":
    result=num1-num2
    print(result)
elif operator == "/":
    result=num1/num2
    print(result)
elif operator == "*":
    result=num1*num2
    print(result)
else:
    print(f"the ${operator} is invalid operator")
    
