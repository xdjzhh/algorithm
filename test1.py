string = input()

newstring = ''

for i in range(len(string)):
    if string[i].isdigit():
        if i == 0 or (not string[i-1].isdigit()):
            newstring+= '*' + string[i]
        else:
            newstring+= string[i]
    else:
        if i == 0:
            newstring += string[i]
            continue
        if string[i-1].isdigit():
            newstring+='*'+string[i]
            continue
        newstring+=string[i]
if newstring[-1].isdigit():
    newstring+='*'
print(newstring)