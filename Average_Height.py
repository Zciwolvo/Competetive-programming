#https://codeforces.com/contest/1509/problem/0


t = int(input())

if 1 <= t and t <= 500:
        while t != 0:
            n = int(input())
            if 2 <= n and n <= 2000:
                a = list(map(int, input().split()))
                if 1 <= len(a) and len(a) <= 2 * 10**5:
                    output = []
                    e = 1
                    while len(a) > 1:
                        if (a[0] + a[e]) % 2 == 0:
                            output.append(a[0])
                            output.append(a[e])
                            a.pop(0)
                            a.pop(e-1)
                            e = 1
                        if len(a) == 1:
                            output.append(a[0])
                            print(' '.join(map(str, output)))
                            t -= 1
                            break
                        if len(a) == 0:
                            print(' '.join(map(str, output)))
                            t -= 1
                            break
                        elif len(a) == 2 and (a[0] + a[1]) % 2 != 0:
                            output.append(a[0])
                            output.append(a[1])
                            print(' '.join(map(str, output)))
                            t -= 1
                            break
                        elif (a[0] + a[e]) % 2 != 0:
                            e += 1

