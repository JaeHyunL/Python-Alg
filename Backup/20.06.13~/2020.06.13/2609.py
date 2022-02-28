def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return int((a/gcd(a, b) * (b/gcd(a, b) * gcd(a, b))))


a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))
