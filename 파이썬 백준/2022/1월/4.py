import sys
from collections import deque

repeat = int(sys.stdin.readline().rstrip())

for _ in range(repeat):
    leng,order = map(int, sys.stdin.readline().rstrip().split())
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    num_goal = n_list[order]
    dict_list = deque()
    for i in range(len(n_list)):
        wow = {
            "order":i,
            "number":n_list[i]
        }
        dict_list.append(wow)
    n_set = sorted(list(set(n_list)), reverse=True)
    count = 0
    index_start = 0
    index_end = len(n_set)-1
    if n_list.count(num_goal) > 1:        
        while 1:
            max_num = n_set[index_start]            
            if dict_list[0]["number"] != max_num:
                dict_list.rotate(-1)
            elif dict_list[0]["number"] == max_num:
                if dict_list[0]["number"] == num_goal:
                    break
                else:
                    count+=1
                    dict_list.remove(dict_list[0])
                    if index_start < index_end:
                        index_start+=1
                    elif index_start == index_end:
                        break
    else:
        n_list.sort(reverse=True)
        a = n_list.index(num_goal)
        print(a)
                           
    print(dict_list,count,n_list,n_set)            
    
    