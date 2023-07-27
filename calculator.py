# Hi, This is a calculator
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
print("Enter which operation you want to do:")
op=input()
if op=="add":
    print(f"The addition of {num1} and {num2} is {num1+num2}")
elif op=="sub":
    if(num1>num2):
        print(f"The subtraction of {num1} and {num2} is {num1-num2}")
    else:
        print(f"The subtraction of {num2} and {num1} is {num2-num1}")
elif op=="mul":
    print(f"The multiplication of {num1} and {num2} is {num1*num2}")
elif op=="div":
    if(num1>num2):
        print(f"The divison of {num1} and {num2} is {num1/num2}")
    else:
        print(f"The divison of {num2} and {num1} is {num2/num1}")
else:
    if(num1>num2):
        print(f"The modulo of {num1} and {num2} is {num1%num2}")
    else:
        print(f"The modulo of {num2} and {num1} is {num2%num1}")