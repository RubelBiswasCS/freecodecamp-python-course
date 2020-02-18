gusses=" "
count=0
haveChance=False

while gusses!="ars" and not(haveChance):
    if(count<3):
        gusses=input("Enter Word : ")
        count += 1

    else :
        haveChance=True



if not(haveChance):
    print("You Win !")
else :
    print("No more Chances...Your Lose")