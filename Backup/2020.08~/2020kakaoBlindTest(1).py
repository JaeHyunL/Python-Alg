
def solution(kstr):
    kstr = kstr.lower()
    # case 1 ,2
    return check1(check1(kstr))


def check1(kstr):
    klist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  '-', '_', '.']
    ans = ''

    for i in range(len(kstr)):
        if kstr[i] in klist:
            ans += kstr[i]
    return check3(ans)


def check3(ans):
    while True:
        ans = ans.replace('..', '.')
        if '..' not in ans:
            break
    return check4(ans)


def check4(ans):
    while True:

        try:
            if ans[0] == '.':
                ans = ans[1:]
        except Exception:
            ans = ''
            break
        try:
            if ans[-1] == '.':
                ans = ans[:-1]
        except Exception:
            ans = ''
            break
        if ans[0] != '.' and ans[-1] != '.':
            break
    return check5(ans)


def check5(ans):
    if ans == '':
        ans = 'a'
    return check6(ans)


def check6(ans):
    if len(ans) >= 16:
        ans = ans[0:15]
    return check7(ans)


def check7(ans):
    while True:
        if len(ans) < 3:
            ans += ans[-1]
        if len(ans) >= 3:
            break

    return ans


print(solution("abcdefghijklmn.p"))
