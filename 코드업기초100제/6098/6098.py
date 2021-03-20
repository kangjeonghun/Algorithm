# 6098 [기초-리스트] 성실한개미
board=[[]*10 for _ in range(10)]
for i in range(10):
    board[i]=list(map(int,input().split()))

x = 1
y = 1

while True:
    # 맨 아래의 가장 오른쪽인 경우 break
    if x == 9 and y == 9:
        print("here is (10,10)")
        break
    # 더 이상 움직일 수 없는 경우 break
    if board[x][y+1] == 1 and board[x+1][y] == 1:
        print("ant can't move anywhere")
        break

    # 오른쪽 이동이 가능하면 현재자리를 9로바꾸고 오른쪽으로 이동
    if board[x][y+1] == 0:
        board[x][y] = 9
        y += 1
    # 오른쪽 이동이 불가능하면 현재자리를 9로바꾸고 아래로 이동
    if board[x][y+1] == 1 and board[x+1][y] == 0:
        board[x][y] = 9
        x += 1

    # 다음공간에 먹이가 있으면 9로바꾸고 break
    if board[x+1][y] == 2:
        board[x][y] = 9
        board[x+1][y] = 9
        break

    if board[x][y+1] == 2:
        board[x][y] = 9
        board[x][y+1] = 9
        break
print(board)