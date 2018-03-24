def solve(N):
    return N

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        N = input().strip()
        n = solve(N)
        print('Case #{}: {}'.format(t, n))