from itertools import permutations     
import sys                
n = sys.stdin.readline().rstrip()
l = len(n)
if l > 10 or int(n) >= 9876543210:
    print(9876543210)
else:
    n = int(n)
    if l == 1:
        print(n)
    else:
        n_list = sorted(list(permutations([str(i) for i in range(10)],r=l)))
        gap = n
        number = 0
        for i in n_list:
            if abs(int("".join(i))-n) < gap:
                gap = abs(int("".join(i))-n)
                number = i
            else:
                break
        print(int("".join(number)))
#1000000000000
#9876543210











