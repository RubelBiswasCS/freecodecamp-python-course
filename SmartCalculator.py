
firstNumber=float(input("Enter First Number"))
op=input("Enter Operetor")
secondNumber=float(input("Enter Second Number"))

if(op=="+"):
    print(firstNumber+secondNumber)
elif(op=="-"):
    print(firstNumber-secondNumber)
elif(op=="*"):
    print(firstNumber*secondNumber)
elif(op=="/"):
    print(firstNumber/secondNumber)
else : print("Wrong Input")