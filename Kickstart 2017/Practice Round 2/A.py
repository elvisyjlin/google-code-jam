def solve():
    S = input()
    L = len(S)
    I, J = map(int, input().split())
    I -= 1
    J -= 1
    if I//L == J//  L:
        num_blue = S[I%L:J%L+1].count('B')
    else:
        num_blue = S[I%L:].count('B') + \
                   S[:J%L+1].count('B') + \
                   S.count('B') * (J//L-I//L-1)
    print(num_blue)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: '.format(t+1), end='')
        solve()