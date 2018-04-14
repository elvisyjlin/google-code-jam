import math

def solve_small():
    # Binary search on rotation
    # Note: Alternative Method
    #       It's easier to calc arccos of the shadow to get (PI/4-theta)
    A = float(input())
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

def rotate(point_yz, angle):
    # Rotate about the x-axis
    # (y', z') = (y * cos(t) + z * sin(t), -y * sin(t) + z * cos(t))
    return (point_yz[0] * math.cos(angle) + point_yz[1] * math.sin(angle), 
           -point_yz[0] * math.sin(angle) + point_yz[1] * math.cos(angle))

def solve():
    EPSILON = 1e-10
    SQRT_2 = math.sqrt(2)
    # Binary search on rotation
    A = float(input())
    l = 0
    r = math.atan(1/math.sqrt(2))
    while l + EPSILON <= r:
        m = (l + r) / 2
        # Area = triangle * 2 + rectangle = diag * (z3-z1)
        z1 = rotate((0.5, 0), m)[1]
        z2 = rotate((-0.5, 0), m)[1]
        z3 = rotate((-0.5, 0.5*SQRT_2), m)[1]
        a = (z3-z1) * SQRT_2
        # print(l, r, z1, z2, z3, a)
        if a - A > EPSILON:
            r = m
        elif A - a > EPSILON:
            l = m
        else:
            break
    print('0 {} {}'.format(*rotate((0.5, 0), m)))
    print('0 {} {}'.format(*rotate((-0.5, 0), m)))
    print('0 {} {}'.format(*rotate((-0.5, 0.5*SQRT_2), m)))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}:'.format(t+1))
        solve()