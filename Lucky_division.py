#https://codeforces.com/problemset/problem/122/A

n = int(input(""))
if 1 <= n and n <= 1000:
    numbers = [4,7,44,47,74,77,444,447,474,477,744,747,777]
    for i in numbers:
        if n % i == 0:
            print("YES")
            break
        elif i == 777 and n % i != 0:
            print("NO")

