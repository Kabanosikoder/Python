Usernum = int (input ("Give me a number: "))
flist = [1]

for x in range (Usernum):
    if x==0:
        flist.append(1)
    else:
        flist.append(flist[-1]+flist[-2])
    
print (flist)
