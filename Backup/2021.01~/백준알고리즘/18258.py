from collections import deque
import sys 

a = deque()
# 
def q_push(index):
    a.append(index)

def q_pop():
    try:
        print(a.popleft())
    except :
        print(-1)

def q_size():
    print(len(a))

def q_empty():
    if len(a) == 0 :
        print(1)
    else :
        print(0)

def q_front():
    if len(a) != 0 :
        print(a[0])
    else : 
        print(-1)
def q_back():
    if len(a) != 0:
        print(a[-1])
    else : 
        print(-1)

for i in range(int(sys.stdin.readline())):
    f = list(map(str, sys.stdin.readline().rstrip().split(' ')))
    if f[0] =='push':
        q_push(f[1])
    elif f[0] == 'pop':
        q_pop()
    elif f[0] == 'size':
        q_size()
    elif f[0] == 'empty':
        q_empty()
    elif f[0] == 'front':
        q_front()
    elif f[0] == 'back':
        q_back()
