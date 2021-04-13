#https://codeforces.com/contest/231/problem/A

n = int(input())
c = n
counter = 0

if 1 <= n <= 1000:
    while c > 0:
        p, v, t = map(int, input().split())
        c -= 1
        if p == 1 and v == 1 or p == 1 and t == 1 or v == 1 and t == 1:
            counter += 1

print(counter)
