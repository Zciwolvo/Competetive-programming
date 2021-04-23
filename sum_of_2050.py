#https://codeforces.com/contest/1517/problem/A
T = int(input())
while T > 0:
    n = int(input())
    count = 0
    while n > 0:
        l = len(str(n))
        l = int(l)
        if l < 4:
            print(-1)
            T -= 1
            break
        l -= 4
        number = 2050 * (10 ** l)
        if n >= number:
            #print(10**l)
            n -= number
            #print(n)
            count += 1
            if n == 0:
                print(count)
                T -= 1
                break
        else:
            l -= 1
            number = 2050 * (10 ** l)
            #print(10**l)
            n -= number
            #print(n)
            count += 1
            if n == 0:
                print(count)
                T -= 1
                break

