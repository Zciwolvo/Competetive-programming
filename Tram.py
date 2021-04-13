n = int(input())
c = n
result = 0
highest_result = 0
if 2 <= n <= 1000:
    while c > 0:
        ai,bi = map(int,input().split())
        c -= 1
        if 0 <= ai <= 1000 and 0 <= bi <= 1000:
            result -= ai
            result += bi
            if result >  highest_result:
                highest_result = result
print(highest_result)

