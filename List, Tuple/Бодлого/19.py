# Нэрсийн бүртгэл өгөгдсөн боловч нэрийн эхний үсэг бүр том биш байв тэдгээрийг том үсэг болго.
# Using Capitalize function
print([name.capitalize() for name in input().split()])

# Traditional Way 
print([name[0].upper() + name[1:] for name in input().split()])
