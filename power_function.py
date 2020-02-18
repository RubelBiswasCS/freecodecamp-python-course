
def raise_power(number,num_power):
    result=1
    for i in range(num_power):
        result=result*number

    return result

print(raise_power(2,3))