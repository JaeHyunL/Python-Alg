# 시간초과 설계를 잘못했넹 .. 

def solution(info, query):
    newlist = []
    newquery = []
    answer = []
    for i in range(len(info)):
        newlist.append(info[i].split(' '))
    for i in range(len(query)):
        newquery.append(query[i].split(' '))
    for i in range(len(newquery)):
        ds = cutline(soulfood(career(position(lang(
            newlist, newquery[i][0]), newquery[i][2]), newquery[i][4]), newquery[i][6]), newquery[i][7])
        answer.append(ds)
    
    return answer


def lang(newlist, str1):
    new2list = []
    for i in range(len(newlist)):
        if newlist[i][0] == str1 or str1 == '-':
            new2list.append(newlist[i])
    return new2list


def position(newlist, str2):
    new2list = []
    for i in range(len(newlist)):
        if newlist[i][1] == str2 or str2 == '-':
            new2list.append(newlist[i])
    return new2list


def career(newlist, str3):
    new2list = []
    for i in range(len(newlist)):
        if newlist[i][2] == str3 or str3 == '-':
            new2list.append(newlist[i])
    return new2list


def soulfood(newlist, str4):
    new2list = []
    for i in range(len(newlist)):
        if newlist[i][3] == str4 or str4 == '-':
            new2list.append(newlist[i])
    return new2list


def cutline(newlist, int1):
    new2list = []
    for i in range(len(newlist)):
        if int(newlist[i][4]) >= int(int1) or int1 == '-':
            new2list.append(newlist[i])
    return len(new2list)
