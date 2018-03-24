def solve():
    N, Q = map(int, input().split())
    ary = list(map(int, input().split()))
    new_array = []
    for i in range(N):
        for j in range(i+1, N+1):
            new_array.append(sum(ary[i:j]))
    new_array = sorted(new_array)
    for _ in range(Q):
        l, r = map(int, input().split())
        print(sum(new_array[l-1:r]))

"""
Two pointer approach

> 1
1: 1*1
> 1 2
1 2 12: 1*2 2*2
> 1 2 3
1 2 12 3 23 123: 1*3 2*4 3*3
> 1 2 3 4
1 2 12 3 23 123 4 34 234 1234: 1*4 + 2*6 + 3*6 + 4*4
...
"""
def solve_better():
    MAX_N = 200000
    MAX_VAL = 100
    pref = []
    def get_sum(l, r):
        return pref[r] - pref[l-1]
    def get_sum_at(idx, n):
        lower = 0
        upper = MAX_N * MAX_VAL
        ans = 0
        while lower <= upper:
            max_val = (lower+upper)//2
            l = 1
            r = 1
            cnt = 0
            add = ary[1]
            ttl = 0
            while r <= n:
                if get_sum(l, r) < max_val:
                    cnt += r - l + 1
                    ttl += add
                    r += 1
                    add += (r - l + 1) * ary[r]
                else:
                    add -= get_sum(l, r)
                    l += 1
                    if l > r:
                        r += 1
                        add = ary[r]
            if cnt >= idx:
                upper = max_val - 1
            else:
                lower = max_val + 1
                ans = ttl + (idx - cnt) * max_val
        return ans
    
    N, Q = map(int, input().split())
    ary = [0] + list(map(int, input().split())) + [0]

    pref.append(0)
    for i in range(1, N+1):
        pref.append(ary[i] + pref[i-1])

    for _ in range(Q):
        l, r = map(int, input().split())
        print(get_sum_at(r, N) - get_sum_at(l-1, N))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}:'.format(t+1))
        # solve()
        solve_better()