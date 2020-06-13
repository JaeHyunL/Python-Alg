# 재귀 호출이란 어떤 함수 안에서 자기 자신을 부르는 것을 말한다. 
# 기억 장소를 다 써버리면 에러를 발생시킨다 

def hello():
    print("hello")
    hello()


hello()
