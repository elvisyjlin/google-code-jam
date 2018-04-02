def prob(N, M, A, B):
    # Recursion form
    if N and M:
        if A > B+1:
            return prob(N-1, M, A+1, B) * N/(N+M) + \
                   prob(N, M-1, A, B+1) * M/(N+M)
        else:
            return prob(N-1, M, A+1, B) * N/(N+M)
    return 1

def prob_faster(N, M):
    # Dynamic programming
    # Init
    table = {}
    table[N, M] = 1
    total = N + M
    # Update
    for pick in reversed(range(total)):
        for n in range(max(pick-M, 0), min(pick+1, N+1)):
            m = pick - n
            a_prob = table[n+1, m] * (N-n)/(total - pick) if n+1 <= N and n+1 > m else 0
            b_prob = table[n, m+1] * (M-m)/(total - pick) if m+1 <= M and n>m+1 else 0
            table[n, m] = a_prob + b_prob
    return table[0, 0]

def solve():
    # A A B A B A B A B ...
    N, M = map(int, input().split())
    # P = prob(N, M, 0, 0)
    P = prob_faster(N, M)
    print('{:.8f}'.format(P))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: '.format(t+1), end='')
        solve()