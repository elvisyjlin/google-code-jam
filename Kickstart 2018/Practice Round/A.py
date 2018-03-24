def solve():
    N = int(input())
    ab = [i for i in map(int, input().split())]
    P = int(input())
    r = []
    for _ in range(P):
        p = int(input())
        count = 0
        for i in range(N):
            if ab[i*2] <= p and ab[i*2+1] >= p:
                count += 1
        r.append(count)
    print(' '.join(map(str, r)))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        if t > 0: input()
        print('Case #{}: '.format(t+1), end='')
        solve()