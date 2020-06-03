def solution(board):
    for j in range(1,len(board)):
        for i in range(1,len(board[0])):
            if board[j][i]:
                board[j][i]=min(board[j-1][i-1],board[j][i-1],board[j-1][i])+1
    ans=0
    for i in board:
        ans=max(max(i),ans)
    return ans

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])