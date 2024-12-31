f = open("DemoText.txt", "r")
print(f.read())  # print(f.read(5)) Эхний 5 тэмдэгт

f = open("DemoText.txt", "r")
print(f.readline()) # Reads line by line

f = open("DemoText.txt", "r")
for x in f:
  print(x)

f = open("DemoText.txt", "r")
print(f.readline())
f.close()


f = open("DemoText2.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("DemoText2.txt", "r")
print(f.read())
f.close()

import os
os.remove("DemoText2.txt")

f = open("Enguunee.txt", "a")
import os
print(os.path.abspath("Enguunee.txt"))