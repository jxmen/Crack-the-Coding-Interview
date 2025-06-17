def calculate(board, y, x):
    # W로 시작하는 체스판과 B로 시작하는 체스판에 대한 다시 칠해야 하는 개수
    count_w_start = 0  # W로 시작하는 체스판
    count_b_start = 0  # B로 시작하는 체스판
    
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            # 현재 위치가 짝수 행 + 짝수 열 또는 홀수 행 + 홀수 열이면 시작 색상과 같아야 함
            if (i - y + j - x) % 2 == 0: # 시작 색상과 같아야 함
                if board[i][j] == 'B':  # W로 시작하는 체스판에서 B면 다시 칠해야 함
                    count_w_start += 1
                if board[i][j] == 'W':  # B로 시작하는 체스판에서 W면 다시 칠해야 함
                    count_b_start += 1
            else:  # 그 외의 경우는 시작 색상과 반대여야 함
                if board[i][j] == 'W':  # W로 시작하는 체스판에서 W면 다시 칠해야 함
                    count_w_start += 1
                if board[i][j] == 'B':  # B로 시작하는 체스판에서 B면 다시 칠해야 함
                    count_b_start += 1
    
    # 두 경우 중 최소값 반환
    return min(count_w_start, count_b_start)
    

def solution(board):
    min_count = float('inf')
    for i in range(n):
        for j in range(m):
            # 체스판의 범위를 벗어나서는 안된다. 범위를 벗어나지 않았을 때만 갱신한다.
            if i + 8 <= n and j + 8 <= m:
                min_count = min(min_count, calculate(board, i, j))
    
    return min_count

n, m = map(int, input().split())

board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(input())

print(solution(board))
