import os
import random



with open('C:/Users/Dell/OneDrive - National University of Mongolia/Desktop/Personal/Coding/Python/Automation Project/Selenium/text.txt', 'r') as file:
    lines = file.readlines()

words = []
for line in lines:
    words.extend(line.split())  

word = random.choice(words).strip().lower()

def formatCheck(word) :
  while len(word)!=5 :
    print("ENTER 5 CHARACTERED WORD")
    word = input()

def checkGreen(user, word) : 
  green = []
  for i in range (len(user)) :
    if(user[i]==word[i]) :
      green.append(i)
  return green  
  
def checkOrange(user, word) :
  orange = []
  for i in range (len(word)) :
    for j in range (len(word)) :
      if(((user[i]==word[j]) and ((j not in green))) and ((j not in orange))) :
        orange.append(i)
  return orange

# Хэрэглэгчээр таалгах үг 
# word = input().lower()


# Defining const 
health = 6 

while(health > 0) :
  # Хэрэглэгч өөрийн үгээ оруулж байна
  user = input().lower()
  formatCheck(user)
  green = []
  green = checkGreen(user, word)
  orange = checkOrange(user, word)
  for i in range (len(word)) :
    if(i in green) :
      print("\033[32m"+ user[i] +"\033[0m", end="")
    elif(i in orange) :
      print("\033[33m"+ user[i] +"\033[0m", end="")
    else :
      print(user[i], end="")
  print()
  if(word == user) :
      print("YOU WINNNN GGG")
      exit
  health-=1
  print()


























