pre = open("input.txt","r")
nex = open("input.txt","r")

preInt = int(pre.readline())
nex.readline()
nex.readline()
nex.readline()
count = 0
while 1 :
    nextLine = nex.readline()
    if not nextLine:
        break
    
    nextInt = int(nextLine)
    if nextInt > preInt :
        count += 1
    preInt = int(pre.readline())

print(count)
pre.close()
nex.close()
