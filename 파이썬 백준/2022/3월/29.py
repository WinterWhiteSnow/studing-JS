# r,l = map(int,input().split())
# n_list = {}
# for _ in range(r):
#     a = list(input())
#     for i in range(len(a)):
#         if i not in n_list:
#             n_list[i] = [a[i]]
#         else:
#             n_list[i].append(a[i])
# string = ""
# for i in range(len(n_list)):
#     not_set = n_list[i]
#     cnt = 0
#     value = []
#     yes_set = list(set(not_set))
#     yes_set.sort()
#     for element in yes_set:
#         if not_set.count(element) > cnt:
#             cnt = not_set.count(element)
#             value = element
#     string+=value
# cnt = 0
# for i in range(len(string)):
#     yes_list = n_list[i]
#     for index in yes_list:
#         if index != string[i]:
#             cnt+=1
# print(string)
# print(cnt) 

# r = lambda : input()
# repeat = int(r())
# a_list = []
# b_list = []
# for _ in range(repeat):
#     wow = float(r())
#     a_list.append(wow)
#     b_list.append(wow)
# for i in range(repeat-1):#index 상승
#     a_list[i]=max(a_list[i],a_list[i]*a_list[i+1])
# for index in range(1,repeat):
#     b_list[index] = max(b_list[index],b_list[index]*b_list[index-1])
# maxi = max(max(a_list),max(b_list))
# print(format(maxi,".3f"))
# for index in range(int(input())):
#     start,end= map(int,input().split())
#     cnt=0
#     for i in range(start,end+1):
#         if str(i) == str(i)[::-1]:
#             if i**(1/2) == int(i**(1/2)):
#                 if str(int(i**(1/2))) == str(int(i**(1/2)))[::-1]:
#                     cnt+=1
#                     # print(i)
#     print(f"Case #{index+1}:",cnt)

# repeat = int(input())
# lestari = {}
# bunga = {}
# for a in range(repeat):
#     a_list = list(map(int,input().split()))
#     lestari[a]=a_list
#     for b in range(repeat):
#         if b not in bunga:
#             bunga[b] = [a_list[b]]
#         else:
#             bunga[b].append(a_list[b])
# b_list = []
# l_list = []
# for i in range(repeat):
#     bunga_list = bunga[i]
#     lestari_list = lestari[i]
#     b_cnt = 1
#     b_now = 0
#     l_cnt = 1    
#     l_now = 0
#     for wow in range(repeat-1):
#         if b_now == 0:
#             if bunga_list[wow]<bunga_list[wow+1]:
#                 b_cnt+=1
#                 b_now = bunga_list[wow+1]
#             else:
#                 b_now = bunga_list[wow]
#         else:
#             if b_now < bunga_list[wow+1]:
#                 b_cnt+=1
#                 b_now = bunga_list[wow+1]
                
#         if l_now == 0:
#             if lestari_list[wow]<lestari_list[wow+1]:
#                 l_cnt+=1
#                 l_now = lestari_list[wow+1]
#             else:
#                 l_now = lestari_list[wow]
#         else:
#             if l_now < lestari_list[wow+1]:
#                 l_cnt+=1
#                 l_now = lestari_list[wow+1]
#     b_list.append(b_cnt)
#     l_list.append(l_cnt)
# print(*b_list)
# for i in l_list:
#     print(i)


                        
        
            
    
    
    

    
    
    
    
    
    