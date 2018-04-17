import math

def solve():
    def find_fail(P_, total_min, total_max, min_max):
        # Results in memory error.
        # print(P_, total_min, total_max, min_max)
        if min_max == []:
            return p
        elif P_ == 0 or P_ >= total_min and P_ <= total_max:
            return P
        elif P_ > total_max:
            return p + total_max * 2
        else:
            res = [find_fail(P_, 
                        total_min-min_max[i][0], 
                        total_max-min_max[i][1], 
                        min_max[:i]+min_max[i+1:]) for i in range(len(min_max))]
            # print(res)
            return max(res)

    def find(cookies, p):
        if p == 0:
            return 0

        S = [[0, 0]]
        for cookie in cookies:
            l, r  = cookie
            S_ = [[s[0]+l, s[1]+r] for s in S if s[0]+l <= p]
            unmerged_idx = list(range(len(S_)))
            for s in S:
                for idx, s_ in enumerate(S):
                    flag = False
                    if s_[0] < s[1] and s_[1] > s[1]:
                        s[1] = s_[1]
                        flag = True
                    if s_[0] < s[0] and s_[1] > s[0]:
                        s[0] = s_[0]
                        flag = True
                    if flag:
                        unmerged_idx.remove(idx)
            for idx in unmerged_idx:
                S.append(S_[idx])

        res = 0
        for s in S:
            res = max(res, min(p, s[1]))
        return res

    def find_knapsack(cookies, p):
        # Modify the problem into the kanpsack problem.
        # The "left bound" is the weight of the item.
        if p == 0:
            return 0

        c = [0] * (p + 1)
        for cookie in cookies:
            l, r = cookie
            for j in reversed(range(l, p+1)):
                c[j] = max(c[j], min(p, c[j-l] + r))
        return c[p]

    N, P = map(int, input().split())
    cookies = []
    p = 0
    # total_min = total_max = 0
    for _ in range(N):
        w, h = map(int, input().split())
        min_v = min(w, h)
        max_v = math.sqrt(w*w+h*h)
        # cookies.append((min_v, max_v))
        cookies.append((min_v*2, max_v*2))
        # total_min += min_v
        # total_max += max_v
        p += 2 * (w + h)
    P_ = (P - p) / 2
    # return find_fail(P_, total_min, total_max, cookies)
    # return p + find(cookies, P_) * 2
    return p + find_knapsack(cookies, P - p)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: {:.6f}'.format(t+1, solve()))