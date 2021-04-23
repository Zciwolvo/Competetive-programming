#https://codeforces.com/problemset/problem/378/A

a,b = input().split()
wina = 0
draw = 0
winb = 0
rolls = [1,2,3,4,5,6]
for n in rolls:
    #print(n)
    diffrencea = int(a) - n
    diffrenceb = int(b) - n
    #print(abs(diffrenceb),abs(diffrencea))
    if abs(diffrencea) < abs(diffrenceb):
        wina += 1
    elif abs(diffrencea) > abs(diffrenceb):
        winb += 1
    else:
        draw += 1
print(wina,draw,winb)


