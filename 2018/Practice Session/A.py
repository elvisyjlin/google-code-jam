def solve():
    while True:
        A, B = map(int, input().strip().split())
        A += 1
        N = int(input())
        while True:
            Q = (A + B) // 2
            print(Q)
            R = input().strip()
            if R == 'TOO_SMALL':
                A = Q + 1
            elif R == 'TOO_BIG':
                B = Q - 1
            elif R == 'CORRECT':
                break
            else:
                raise Exception(R)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        solve()