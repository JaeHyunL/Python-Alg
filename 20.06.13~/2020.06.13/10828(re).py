import sys


def pop():
    try:
        print(nlist.pop())
    except:
        print(-1)


def top():
    if len(nlist) != 0:
        print(nlist[len(nlist)-1])
    elif len(nlist) == 0:
        print(-1)


def push(n):
    nlist.append(n)


def size():
    print(len(nlist))


def empty():
    if len(nlist) == 0:
        print(1)
    else:
        print(0)


n = int(sys.stdin.readline())
nlist = []
for i in range(n):
    inp = sys.stdin.readline().split()
    if inp[0] == 'push':
        push(inp[1])
    if inp[0] == 'top':
        top()
    if inp[0] == 'size':
        size()
    if inp[0] == "empty":
        empty()
    if inp[0] == "pop":
        pop()
