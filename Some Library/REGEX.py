# Regex нь тэмдэгт мөрийг тухайн загварт нийцэж байгаа эсэхийг шалгахад ашигладаг
# Тухайлбал цахим хаяг , утасны дугаар , регистрийн дугаар гэх мэт тэмдэгт нь загварт тохирож байгаа эсэхийг шалгадаг

import re

# Return a list containing every occurance of "ai" :
str = "The rain in Spain"
x = re.findall("ai", str)
print(x) # [ai , ai]

# Split the string at every white-space character :
str = "The rain in Spain"
x = re.split("\s", str) # \s means whitespace which is space 
print(x)

# Replace all white-space character with the digit "9" :
str = "The rain in Spain "
x = re.sub('\s', "9", str)
print(x)





# METACHAR CHARACTER

str = "abcddddefghijklmnocdrscuvdwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
x = re.sub('[a-m]',"0", str) # Replacing all character that are in between a to m by 0
print(x)
x = re.sub('^[a-m]',"0", str) # Replacing if string is started with character that are in between a to m by 0
print(x)
x = re.sub('[0-9]$',"0", str) # Replacing if string's last character that are in between a to m by 0
print(x)
x = re.sub('cd+',"0", str) # if string has exactly one "c" followed by one or more "d"'s it will replace those with "0"
print(x) # minimum occurance of d is has to be atleast 1 .
x = re.sub('cd*',"0", str) # if string has exactly one "c" followed by zero or more "d"'s it will replace those with "0"
print(x) # minimum occurance of "d" is "0" .



# SET OF METACHAR CHARACTER
 
# [arn] contains a , r  or n 
# [a-n] contains character that in between a to n
# [^arn] contains any other characters than a , r or n
# [0123] contains one of given character (Basically same as first one im just lazy)
# [0-9] contains character that in 1 to 9 (Also same as second one)
# [0-5][0-9] contains number between 00-59 (first [] represents first digit and others like that )
# [a-zA-z] contains "Toм жижиг үсэг "


# SPECIAL CHARACTERS
# Character   Example   Description
#    \A      "\AGood"   Checks if its starts with "Good"
#    \d        "\d"     Checks if that row is contains any digit (Works same as [0-9])
#    \D        "\D"     its literally negative(\d) checks if that row doesnt contain any digit
#    \s        "\s"     Checks if its contains whitespace 
#    \S        "\S"     Checks if its doesnt contain whitespace
#    \w        "\w"     Checks if its contains Capital letter, small letter and underline
#    \Z        "hah\Z"  Checks if its ends with "hah"



# Important Example

import re
s = "My 2 favourite numbers are 7 and "
list = re.findall('[0-9]+', s) # String has to contain atleast one character that in 0 to 9
print(list)


import re
s =  "Hello from enguunbayyr@gmail.com to 23b1num0002@stud.num.edu.mn about the meetung @2PM"
list = re.findall('\S+@\S+', s) # Урд ард талдаа ямар нэгэн тэмдэгтэй @ тэмдэгийг хайж байна
print(list)


# Өгөгдсөн тэмдэгт мөрөөс утасны дугаарыг олох 
str = "Hello my name is Enguunbayar and im 20 . If u want to contact me call me +97688999419.  My gmail is enguunbayyr@gmail.com ."
list = re.findall('[+][0-9]+', str) # Phone number should starts with + and following atleast one character should be number .
print(list)

# Өгөгдсөн тэмдэгт мөрөөс и-мэйл олох
str = "Hello my name is Enguunbayar and im 20 . If u want to contact me call me +97688999419.  My gmail is enguunbayyr@gmail.com ."
list = re.findall('\S+@\S+', str) # E-mail should contain certain character "@" .

# Өгөгдсөн тэмдэгт мөрөөс регистрийн дугаар олох
str = '''Hello my name is Enguunbayar and im 20 . 
If u want to contact me call me +97688999419.  My gmail is enguunbayyr@gmail.com . 
My social security number is UP052703919 '''
list = re.findall('[A-Z][A-Z][0-9]+', str) # SSN number should start with 2 Capital alphabet following numbers
print(list)
