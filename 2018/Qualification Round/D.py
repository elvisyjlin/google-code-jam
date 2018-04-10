import math

def solve():
    A = float(input())
    if A < 1.414214:
        l = 0
        r = math.pi / 4
        while l <= r:
            m = (l + r) / 2
            a = math.sin(m) + math.cos(m)
            if a - A > 0:
                r = m
            elif A - a > 0:
                l = m
            else:
                break
        print('{} {} 0'.format(0.5*math.cos(m), 0.5*math.sin(m)))
        print('{} {} 0'.format(-0.5*math.sin(m), 0.5*math.cos(m)))
        print('0 0 0.5')
    else:
        pass

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}:'.format(t+1))
        solve()