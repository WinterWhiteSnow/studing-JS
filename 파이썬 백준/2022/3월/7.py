# a_list =[]
# r= int(input())
# for _ in range(r):
#     a_list.append(int(input()))
# a_list = a_list[::-1]
# cnt = 0
# for i in range(1,len(a_list)):
#     wow = a_list[i-1:i+1]
#     a = wow[0]
#     b = wow[1]
#     # print(wow)
#     if a>b:
#         pass
#     else:
#         correct = a-1
#         cnt+=b-correct
#         a_list[i]=correct
#         # print(a_list)
# print(cnt)    

a = list(input())
b = set(a)
one_list = []
a_dict = {}
for i in b:
    if a.count(i)%2 == 0:
        pass
    else:
        one_list.append(i)
        if len(one_list) > 1:
            print("I'm Sorry Hansoo")
            exit()
    a_dcit[i]=a.count(i)
    
# if len(one_list) > 0:
#     for i in 
# 나온횟수 많은순서대로 히나씩
        