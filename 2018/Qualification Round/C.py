def solve():
    A = int(input())
    row = (A + 2) // 3 # from (100 100) to (100+row-1, 100)
    board = []
    for _ in range(1000):
        board.append([0]*1000)
    I = J = 100 # [2, 999]
    for _ in range(1000):
        print('{} {}'.format(I, J))
        I_, J_ = map(int, input().split())
        if I_ == 0 and J_ == 0:
            return
        board[I_][J_] = 1
        while board[I-1][J-1] and board[I-1][J] and board[I-1][J+1] and I < 100+row-3:
            I += 1
    input()

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        solve()