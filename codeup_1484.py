# Codeup_Python 기초5-3.2차원배열_1484: 2차원 배열 달팽이 채우기 4-1

n,m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
direct = [(0,1),(1,0),(0,-1),(-1,0)]
direct_idx = 0
row = 0
col = 0

for num in range(1,n*m+1):
    arr[row][col] = num

    next_row = row + direct[direct_idx][0]
    next_col = col + direct[direct_idx][1]

    if next_row <0 or next_col <0 or next_row>=n or next_col>=m or arr[next_row][next_col] !=0 :
        direct_idx = (direct_idx+1)%4
    row += direct[direct_idx][0]
    col += direct[direct_idx][1]
for i in arr:
    print(*i)