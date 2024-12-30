list_name = input().split()
b_list = []

# Iterate through list_name using an index
index = 0
while index < len(list_name):
    if list_name[index].find("b")!=-1 or list_name[index].find("B")!=-1:  # Check for 'b' or 'B'
        b_list.append(list_name[index])
        list_name.remove(list_name[index])  # Remove the name with 'b'
    else:
        index += 1  # Only increment index if no removal

print(list_name)
print(b_list)
