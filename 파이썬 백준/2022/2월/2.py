a_list = []
cnt = 0
for _ in range(10):
    a = int(input())
    cnt+=a
    a_list.append(a)
print(cnt//10)
a_set = set(a_list)
a_dict = {}
for i in a_set:
    a_dict[i]=a_list.count(i)
wow = sorted(a_dict.items(), key = lambda x : x[1], reverse=True)
print(wow[0][0])
