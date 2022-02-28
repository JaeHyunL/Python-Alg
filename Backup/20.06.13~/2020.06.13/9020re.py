import sys
 
## 애초에 함수로 돌리지말고 그냥 for 문을 처음 써놔서 리스트를 만들어서 반복시킨다 
# 굿 아이디어 ..
# 참조 https://developmentdiary.tistory.com/271
prime_number=[2 for _ in range(10001)]
 
for i in range(1,10001):       
    if i==1:
        prime_number[i]=0
    elif prime_number[i]!=0:
 
        prime_number[i]=1
        mul = 2
        j = i
        while(j*mul<=10000):
            prime_number[j*mul]=0
            mul+=1
 
T=int(sys.stdin.readline())
while(T>0):
    T-=1
    n=int(sys.stdin.readline())
    mid=n//2
    x=0
    for i in range(0,mid):  
        if prime_number[mid+x]+prime_number[mid-x]==2:
            print(str(mid-x)+" "+str(mid+x))
            break
        x+=1
 