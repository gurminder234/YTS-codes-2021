n = int(input("= "))

m = int(pow(n,0.5))
e = n+1
l = []

for p in range(2, e):
    l.insert(0,2)
    l.insert(1,3)
    l.append(p)

    for i in range(2, m + 1):
        for j in range(i, n+1, i):
            if j in l:
                l.remove(j)

print(l)


