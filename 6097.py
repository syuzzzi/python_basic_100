h, w = map(int, input().split())  # 격자판의 세로와 가로 입력
n = int(input())  # 놓을 막대 개수

# 세로(h) * 가로(w) 크기의 2차원 리스트(격자판) 초기화
a = [[0] * (w + 1) for _ in range(h + 1)]

# 각 막대의 위치와 방향을 입력받아 격자판에 막대 배치
for _ in range(n):
    l, d, x, y = map(int, input().split())  # 막대 길이, 방향, 시작 좌표
    
    if d == 0:
        # 수평 막대
        for j in range(l):
            a[x][y + j] = 1
    elif d == 1:
        # 수직 막대
        for i in range(l):
            a[x + i][y] = 1

# 격자판 출력
for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(a[i][j], end=' ')
    print()