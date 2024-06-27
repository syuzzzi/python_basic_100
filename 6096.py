def toggle(board, x, y):
    for i in range(19):
        if i != y:
            # 가로줄 뒤집기 (x번 줄에서 y를 제외한 부분)
            board[x][i] = 1 - board[x][i]
        if i != x:
            # 세로줄 뒤집기 (y번 열에서 x를 제외한 부분)
            board[i][y] = 1 - board[i][y]

# 바둑판 초기화
board = []
for _ in range(19):
    row = list(map(int, input().split()))
    board.append(row)

# 십자 뒤집기 횟수 입력 받기
n = int(input())

# 십자 뒤집기 좌표 입력받아 처리
for _ in range(n):
    x, y = map(int, input().split())
    # 입력 좌표는 1부터 시작하므로 인덱스를 0부터 시작하는 방식으로 변환
    toggle(board, x - 1, y - 1)

# 결과 출력
for row in board:
    print(' '.join(map(str, row)))