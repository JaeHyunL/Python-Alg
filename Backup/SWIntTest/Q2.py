
def oddNumbers(l, r):
    ad = []
    for i in range(l,r+1):
       if i %2 ==1 :
           ad.append(i) 
    return ad

print(oddNumbers(3,7))