
def change(word):
    changed=""
    for letter in word:
        if letter.lower() in "aeiou":

            if letter.isupper():
                changed=changed+"L"
            else :
                changed=changed+"l"
        else :
            changed = changed+letter
    return changed

print(change(input("Enter a Word : ")))