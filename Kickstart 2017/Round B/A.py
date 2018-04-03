BASE = 1e9+7

def preprocess(N):
    p = [1]
    for i in range(1, N):
        p.append(p[i-1]*2 % BASE)
    return p

def solve():
    N = int(input())
    p = preprocess(N)
    K = list(map(int, input().split()))
    R = 0
    for i in range(N):
        R = (R + (p[i] - p[N-i-1]) * K[i]) % BASE
    print(int(R))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: '.format(t+1), end='')
        solve()