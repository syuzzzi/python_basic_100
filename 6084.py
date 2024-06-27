h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

k = h*b*c*s/8/1024/1024

print(format(k, ".1f"), "MB")