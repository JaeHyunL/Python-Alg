def a(num_list):
    b = 0
    for i in num_list:
        b += i
    return b


if __name__ == "__main__":
    k = int(input())
    print(a(k))
