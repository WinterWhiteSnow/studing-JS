import sys
sys.setrecursionlimit(10**6)
n = int(input())
wow = [0]*(n+1)

def why(num):
    if wow[num] != 0:
        return wow[num]
    elif num == 0:
        return 0
    else:
        if num == 1 or num == 2:
            wow[num]=1
            return wow[num]
        wow[num]=why(num-1)+why(num-2)
        return wow[num]

print(why(n),n-2)