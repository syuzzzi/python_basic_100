c = int(input())
n = input().split()

for i in range(c):
    n[i] = int(n[i])
    
d = []

for i in range(24):
    d.append(0)
    
for i in range(c):
    d[n[i]] += 1 
    
for i in range(1, 24):
    print(d[i], end=' ')