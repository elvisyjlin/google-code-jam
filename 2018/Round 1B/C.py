def solve():
    M = int(input())
    R = []
    for i in range(M):
        r1, r2 = map(int, input().split())
        R.append((r1, r2))
    G = list(map(int, input().split()))

    def check(m):
        if G[0] >= m:
            return True

        temp = list(G)
        limit = sum(temp)
        temp[0] = 0
        temp[R[0][0]-1] += G[0] - m
        temp[R[0][1]-1] += G[0] - m
        
        i = 0
        while True:
            flag = True
            i += 1
            for i, t in enumerate(temp):
                if t < 0:
                    temp[i] = 0
                    temp[R[i][0]-1] += t
                    temp[R[i][1]-1] += t
                    flag = False
                if t < -limit:
                    return False
            if flag:
                return True

    l = 0
    r = 1e20
    largest = 0
    while l < r:
        m = (l + r) // 2
        if check(m):
            largest = max(largest, m)
            l = m + 1
        else:
            r = m
    print(int(largest))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: '.format(t+1), end='')
        solve()