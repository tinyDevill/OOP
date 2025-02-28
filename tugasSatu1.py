n = int(input("Height: "))
s = "*"

if n > 1:
    base = 1 + pow(2, n - 1)
else:
    base = n

for _ in range(n):
    print(s.center(base))
    s += "**"