def getint(txt):
    return int (input(txt+' '))

def getstr(txt):
    return input(txt+ ' ')

#name=getstr("Give me your name")
#name2=getstr("Give me another name")

num=getint("Give me a number")
#age=getint("Give me your age")
for x in range(num + 1,1,-1):
    if num % x == 0:
        print(x)

