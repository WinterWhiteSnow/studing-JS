import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

r = one()
number =r
n_list = [one() for _ in range(r)]
answer_list = [i for i in range(1,r+1)]
cnt = 0
state_dict = {}
max_num = 0
for i in range(r-1,-1,-1):
    if n_list[i] == number:
        number-=1
        max_num+=1
print(r-max_num)
    
        
            
        

























