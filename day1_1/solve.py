file = open("input.txt","r")

preInt = int(file.readline())
count = 0
while 1 :
    nextLine = file.readline()
    if not nextLine:
        break
    
    nextInt = int(nextLine)
    if nextInt > preInt :
        count += 1
    preInt = nextInt

print(count)
file.close()
