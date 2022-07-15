import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n,m=wow()
# maxi_num = max(n,m)
# n_list = [0]*(maxi_num+1)
# cnt = 1
# for i in range(1,maxi_num+1):
#     cnt*=i
#     n_list[i]=cnt
# print(n_list[n]//n_list[n-m]//n_list[m])
sys.setrecursionlimit(10**6)
list_list = [5,7,2,0,3,1,6,9,4,8]
def why(array):
    print("start",array)
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    print("left!!!",left_side)
    print("right!!!",right_side)
    return why(left_side)+[pivot]+why(right_side)
print(why(list_list))











