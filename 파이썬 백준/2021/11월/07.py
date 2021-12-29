# a = list(range(1,10))
# b = [7,8,9,4,5,6,1,2,3]
# c = {}
# for i in range(len(b)):
# 	c[a[i]]=b[i]

# answer_list = []
# count = 0
# while count !=7:
# 	count +=1
# 	answer = int(input())
# 	answer_list.append(c[answer])
# for i in answer_list:
# 	print(i, end="")

# count = 0
# a_list = []
# while count != 10:
# 	count +=1
# 	a = int(input())
# 	a_list.append(a%42)
# a_list = set(a_list)
# print(len(a_list))

the_num = int(input())
count = 0
a =input().split()
if len(a) == the_num:
	a = [int(i) for i in a]
	a.sort()
	print(sum(a)/a[-1])