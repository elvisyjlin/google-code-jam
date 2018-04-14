def solve_bs():
    # Helper function
    def calc(t):
        cashers = []
        for i in range(C):
            cashers.append(f(t, i))
        selected_cashers = sorted(cashers, reverse=True)[:R]
        return sum(selected_cashers)
    def f(t, casher_idx):
        return max(0, min(M[casher_idx], (t-P[casher_idx])//S[casher_idx]))
    # Read input
    R, B, C = map(int, input().split())
    M, S, P = [], [], []
    for i in range(C):
        m, s, p = map(int, input().split())
        M.append(m)
        S.append(s)
        P.append(p)
    # Binary search on time
    l = 0
    r = 1e19
    while l < r:
        m = (l + r) // 2
        max_bits = calc(m)
        if max_bits >= B:
            r = m
        else:
            l = m + 1
    return r

def solve_fail():
    R, B, C = map(int, input().split())
    # Prepare cashers
    cashers = []
    for i in range(C):
        m, s, p = map(int, input().split())
        r = [s*(i+1)+p for i in range(m)]
        cashers.append(r)
    # Choose cashers
    exp_b = (B+R-1) // R
    cashers = sorted(cashers, key=lambda x: x[exp_b] if exp_b<len(x) else x[-1])
    cashers = cashers[:R]
    # However, there is no proper way to find the R robots.
    # Robots spend
    time_spent = 0
    while B > 0:
        cashers = sorted(cashers, key=lambda x: x[0])
        idx = 0
        while cashers[idx][0] <= time_spent:
            cashers[idx].pop(0)
            if cashers[idx] == []:
                cashers.pop(idx)
            B -= 1
            idx += 1
            if B == 0:
                return time_spent
        time_spent = cashers[idx].pop(0)
        if cashers[idx] == []:
            cashers.pop(idx)
        B -= 1
    return time_spent

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: {}'.format(t+1, solve_bs()))