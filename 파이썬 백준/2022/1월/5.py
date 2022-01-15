# import sys
# from collections import deque

# repeat = int(sys.stdin.readline().rstrip())

# for _ in range(repeat):
#     leng,order = map(int, sys.stdin.readline().rstrip().split())
#     n_list = list(map(int, sys.stdin.readline().rstrip().split()))
#     num_goal = n_list[order]
#     dict_list = deque()
#     for i in range(len(n_list)):
#         wow = {
#             "order":i,
#             "number":n_list[i]
#         }
#         dict_list.append(wow)
#     order_list = []      
#     while 1:
#         max_max = max(dict_list, key = lambda x : x["number"])
#         max_num = max_max["number"]  
#         if dict_list[0]["number"] != max_num:
#             dict_list.rotate(-1)
#         elif dict_list[0]["number"] == max_num:
#             order_list.append(dict_list[0]["order"])
#             dict_list.remove(dict_list[0])
#         if len(dict_list) == 0:
#             break
#     print(order_list.index(order)+1)    

import sys

wow = int(sys.stdin.readline().rstrip())
num_list = [i for i in range(1,wow+1)]
a_list = []
for _ in range(wow):
    d = int(sys.stdin.readline().rstrip())
    a_list.append(d)

first_step = []
text = []
second_step = []


a_index = 0
index = 0
while True:
    # standard = 넣고 빼는 기준, 1이면 넣고 2면 뺀다.
    standard = 1
    lala = "wow"
    if len(second_step) == len(a_list):
        break
    if lala == "IndexError":
        print("NO")
        break 
    
    print(first_step,second_step,"index:",index,"a_index:",a_index)
    if standard == 1:
        while True:
            if index == len(num_list):
                standard=2
                break
            first_num = num_list[index]
            if a_list[a_index] >= first_num:
                first_step.append(first_num)
                text.append("+")
                index+=1
            else:
                standard = 2
                break 
    print("1완료",first_step)  
    
    if standard == 2:
        while True: 
            if a_index == len(num_list):
                break   
            print("a_index:",a_index,first_step,second_step)
            if first_step:
                if first_step[-1] == a_list[a_index]:
                    second_step.append(first_step.pop())
                    text.append("-")
                    a_index+=1  
                else:
                    standard=1
                    break
            else:
                print("else!!!","a_index:",a_index,first_step,second_step)
                break
print(first_step,second_step,text)        

#오답 무한루프 수정필요

    
    
    
            
        
    
        
        
    