import sys

repeat = int(sys.stdin.readline().rstrip())

for _ in range(repeat):
    x,y,r1,a,b,r2 = map(int, sys.stdin.readline().rstrip().split())
    distance_x = (a-x)**2
    distance_y = (b-y)**2
    distance = distance_x+distance_y
    radius = (r2+r1)**2
    r_list = [r1,r2]
    r_list.sort()
    mini_r = r_list[0]
    max_r = r_list[-1]

    if (max_r-mini_r)**2<distance<(max_r+mini_r)**2:
        print(2)
    elif (max_r-mini_r)**2 == distance != 0 or (max_r+mini_r)**2== distance != 0: 
        print(1)
    elif (max_r-mini_r)**2 == distance == 0 or (max_r+mini_r)**2== distance == 0 :
        print(-1)
    else:
        print(0)
# 50%