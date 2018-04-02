def solve():
    N = int(input())
    leader = ''
    max_diff = 0
    for _ in range(N):
        name = input().strip()
        s = set(name)
        if ' ' in s:
            s.remove(' ')
        num_diff = len(s)
        if num_diff > max_diff:
            max_diff = num_diff
            leader = name
        elif num_diff == max_diff and name < leader:
            max_diff = num_diff
            leader = name
    print(leader)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: '.format(t+1), end='')
        solve()