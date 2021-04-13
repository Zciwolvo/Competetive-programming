n = int(input())
c = n
result = 0
l = []
if 2 <= n <= 30:
    while c > 0:
        hi,ai = map(int,input().split())
        c -= 1
        if 0 <= hi <= 1000 and 0 <= ai <= 1000:
            l.append(hi)
            l.append(ai)

l_1 = []
l_2 = []
len = len(l)
while len > 0:
    l_1.append(l[0])
    l.pop(0)
    l_2.append(l[0])
    l.pop(0)
    len -= 2


for i in l_1:
    for j in l_2:
        if i == j:
            result += 1
print(result)