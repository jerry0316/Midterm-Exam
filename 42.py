a = int(input())
b = int(input())
c = int(input())
ans = b**2 - 4*a*c
if ans > 0:
    print(int((-b + pow(b**2 - 4*a*c,0.5))/(2*a)))
    print(int((-b - pow(b**2 - 4*a*c,0.5))/(2*a)))
elif ans == 0:
    print(int(-b / (2*a)))
else:
    print(0)