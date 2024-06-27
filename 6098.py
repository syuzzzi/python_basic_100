d = []

# 미로 정보 입력 받기
for i in range(10):
    d.append(list(map(int, input().split())))

x = 1
y = 1

d[x][y] = 9

while True:
    if d[x][y+1] == 0 or d[x][y+1] == 2:
        y += 1
        if d[x][y] == 2:
            d[x][y] = 9
            break
        d[x][y] = 9
    elif d[x+1][y] == 0 or d[x+1][y] == 2:
        x += 1 
        if d[x][y] == 2:
            d[x][y] = 9
            break
        d[x][y] = 9
    else:
        break

# 결과 출력
for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()