n = int(input())
s = 0
c = 1 

while 1 :
    s += c 
    c += 1 
    
    if s>=n:
        break
    
print(s)