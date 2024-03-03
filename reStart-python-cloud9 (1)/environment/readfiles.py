print("Here is my diary: \n")

f1 = open("files/diary.txt", "r")
print(f1.read())
f1.close()

print("\n create another diary")

f2 = open("files/diary2.txt", "w")
f2.write("writing in my diary file")

f2.close()

f3 = open("files/diary3.txt", "w")
f3.write("writing in my diary file")

f3.close()

