import sys
nlist = []
slist = []
n = int(sys.stdin.readline())
for i in range(n):
    stackCode = sys.stdin.readline().split()
    if len(stackCode) == 2:
        nlist.append(stackCode[1])
    if len(stackCode) == 1:
        if stackCode[0] == "top":
            if len(nlist) != 0:
                print(nlist[len(nlist)-1])
            elif len(nlist) == 0:
                print(-1)
        elif stackCode[0] == 'size':
            print(len(nlist))
        elif stackCode[0] == 'empty':
            if len(nlist) == 0:
                print(1)
            else:
                print(0)
        if stackCode[0] == 'pop':
            try:
                print(nlist.pop())
            except:
                print(-1)
