

def max_number(num1,num2,num3):
    if(num1 >= num2 and num1>=num3):
        return num1
    elif (num2 >= num1 and num2>=num3):
        return num2
    else:
        return num3

def input_fuc():
    print("Enter 3 Numbers")
    a=input()
    b=input()
    c=input()
    print("Max number is : " + max_number(a, b, c))


input_fuc()


