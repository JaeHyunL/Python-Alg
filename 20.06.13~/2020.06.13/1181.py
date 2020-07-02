a = int(input())

wordlist = {}

for i in range(a):
    b = input()
    wordlist[b] = len(b)
wordlist = sorted(wordlist.items(), key=lambda x: x[0])
wordlist = dict(wordlist)
wordlist = sorted(wordlist.items(), key=lambda x: x[1])

wordlist = dict(wordlist)
for i in wordlist.keys():
    print(i)

