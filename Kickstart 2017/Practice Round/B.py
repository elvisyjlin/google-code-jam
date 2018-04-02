def prob(N, M, A, B):
    # Recursive form
    if N and M:
        if A > B+1:
            return prob(N-1, M, A+1, B) * N/(N+M) + \
                   prob(N, M-1, A, B+1) * M/(N+M)
        else:
            return prob(N-1, M, A+1, B) * N/(N+M)
    return 1

def solve():
    # A A B A B A B A B ...
    N, M = map(int, input().split())
    P = N/(N+M) if N else 0
    P *= prob(N-1, M, 1, 0)
    print('{:.8f}'.format(P))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: '.format(t+1), end='')
        solve()