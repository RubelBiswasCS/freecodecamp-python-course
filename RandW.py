

#fileopen = open("new_txt.txt","a")

#fileopen.write("\nThis is stil a text file")
#print(fileopen.read())

#fileopen.close()

file = open("testfile.txt", "r+")

file.write("Hello World")
file.write("This is our new text file")
file.write(" and this is another line.")
file.write("Why? Because we can.")

print(file.read())

file.close()