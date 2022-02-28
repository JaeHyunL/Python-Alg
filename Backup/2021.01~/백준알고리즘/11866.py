a , k = map(int,input().split())

alist = [ _ for _ in range(1,a+1)]
index = -1
answer = []

for i in range(a):
    index += k
    if index >= len(alist) :
        index %= len(alist)
    answer.append(str(alist.pop(index)))
    index -=1 

print("<",", ".join(answer),">",sep='')
 