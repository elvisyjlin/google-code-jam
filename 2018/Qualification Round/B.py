def solve():
    N = int(input())
    V = list(map(int, input().split()))
    V1 = sorted(V[::2])
    V2 = sorted(V[1::2])
    flag = -1
    for i in range(1, N):
        i_ = i // 2
        # if i&1: print('Check {} {}'.format(V1[i_], V2[i_]))
        # if i&1==0: print('Check {} {}'.format(V2[i_-1], V1[i_]))
        if i&1 and V1[i_] > V2[i_] or i&1==0 and V2[i_-1] > V1[i_]:   # odd
            flag = i - 1
            break
    print('OK') if flag == -1 else print(flag)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: '.format(t+1), end='')
        solve()