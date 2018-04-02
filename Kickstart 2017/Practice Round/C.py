def nCr(n,r):
    import math
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def solve():
    # Form of ()()()()()... maximize the possible combinations
    L, R = map(int, input().split())
    pair = min(L, R)
    return nCr(pair+1, 2) if pair else 0

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = solve()
        print('Case #{}: {}'.format(t+1, n))