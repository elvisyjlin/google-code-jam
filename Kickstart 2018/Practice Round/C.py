def solve():
    N = int(input())
    trip = {}
    srcs = set()
    dsts = set()
    for _ in range(N):
        src = input()
        dst = input()
        trip[src] = dst
        srcs.add(src)
        dsts.add(dst)
    start = [i for i in srcs if i not in dsts][0]
    result = []
    while start in trip:
        result.append('{}-{}'.format(start, trip[start]))
        start = trip[start]
    print(' '.join(result))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: '.format(t+1), end='')
        solve()