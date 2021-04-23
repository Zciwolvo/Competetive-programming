#https://codeforces.com/problemset/problem/9/A

Y,W = input().split()

if Y > W:
    better_roll = int(Y)
else:
    better_roll = int(W)

propability = 7 - better_roll

if propability == 1:
    print("1/6")
elif propability == 2:
    print("1/3")
elif propability == 3:
    print("1/2")
elif propability == 4:
    print("2/3")
elif propability == 5:
    print("5/6")
elif propability == 6:
    print("1/1")