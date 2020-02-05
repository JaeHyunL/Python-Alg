def a(k):
    b = 0
    for i in k:
        b += i
    return b


if __name__ == "__main__":
    k = int(input())
    print(a(k))
