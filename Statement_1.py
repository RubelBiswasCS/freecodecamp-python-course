
isMale=False
isTall=False

if isMale and isTall:
    print("male and tall")
elif isMale and not(isTall):
    print("male but not tall")
elif not(isMale) and isTall:
    print("Not male but tall")
else: print("Neither male nor tall")