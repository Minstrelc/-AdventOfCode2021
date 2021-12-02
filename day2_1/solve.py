file = open("input.txt","r")

horizontal = 0
depth = 0

while 1 :
    nextLine = file.readline()
    if not nextLine:
        break

    lineData = nextLine.split()
    if(lineData[0][0]=='f'):
        horizontal += int(lineData[1])
        continue
    
    if(lineData[0][0]=='d'):
        depth -= int(lineData[1])
        continue

    if(lineData[0][0]=='u'):
        depth += int(lineData[1])
        continue
    
print(horizontal * depth)

file.close()
