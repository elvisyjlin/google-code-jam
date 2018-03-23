def isOdd(d):
    return d % 2 == 1

def solve(N):
    for i in range(len(N)):
        d = int(N[i])
        if isOdd(d):
            rest = len(N)-i-1
            if d != 9:
                upper = str(d+1) + '0'*rest
            else:
                # # To find the upper bound when there is a carry
                # prefix = ''
                # j = i-1
                # while j>=0 and N[j]=='8':
                #     prefix = '0' + prefix
                #     j -= 1
                # if j >= 0:
                #     prefix = str(int(N[j])+2) + prefix
                # else:
                #     prefix = '2' + prefix
                # upper = prefix + str(d+1) + '0'*rest

                # While there is no need to do so because the upper won't be the answer
                upper = '1' + '0' * 17
            lower = str(d-1) + '8'*rest
            return min(int(upper)-int(N[i:]), int(N[i:])-int(lower))
    return 0

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        N = input().strip()
        n = solve(N)
        print('Case #{}: {}'.format(t, n))