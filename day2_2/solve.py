def solve(path):
    file = open(path,"r")

    aim = 0
    horizontal = 0
    depth = 0

    while 1 :
        nextLine = file.readline()
        if not nextLine:
            break

        lineData = nextLine.split()
        if(lineData[0][0]=='f'):
            x = int(lineData[1])
            horizontal += x
            depth += aim * x
            continue
        
        if(lineData[0][0]=='d'):
            aim += int(lineData[1])
            continue

        if(lineData[0][0]=='u'):
            aim -= int(lineData[1])
            continue
        
    print(horizontal * depth)

    file.close()

solve("input.txt")
#solve("sample.txt")
