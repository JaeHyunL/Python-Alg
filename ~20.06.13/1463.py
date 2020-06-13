#
# X가 3으로 나누어떨어지면 /3
# X가 2으로 나누어떨어지면 /2
# 1을 뺀다

n = int(input())
n2 = 0
count = 0


while True : 
    if n - 1 % 3 == 0 : 
        if (n-1/3) % 3 == 0 :
            print('1빼는게 쌉이득') 
        elif (n-1/3) %2 == 0 :
            print("안빼는게 쌉이득 ")