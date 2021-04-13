#https://codeforces.com/contest/4/problem/A

w = int(input(""))

if 1 <= w and 100 >= w:
    if w % 2 == 0 and w > 2:
        print("YES")
    else:
        print("NO")
else:
    print("that's not a proper weight")