def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        print(s[1:]+s[0])
        return reverse_string(s[1:]) + s[0]
print(reverse_string("Enguunbayar"))