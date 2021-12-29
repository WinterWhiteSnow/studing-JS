import sys

list_list = {}
for i in range(2,10000+1):
	if i not in list_list:
		for a in range(i,10000+1,i):
			list_list[a]=1
		list_list[i]=0

result_list = {}
for key,value in list_list.items():
	if value == 0:
		result_list[key] = value

answer_sort = sorted(result_list.keys())
the_num = int(sys.stdin.readline())

count =0
answer_list = []
while count != the_num:
	count +=1
	answer = int(sys.stdin.readline())
	answer_list.append(answer)
list_list_list = []
for a in answer_list:
	wow = []
	for b in answer_sort:
		if 2 <a-b < a and a-b in answer_sort:
			wow.append(a-b)
	if len(wow)%2 == 0:
		print(wow[len(wow)//2],wow[len(wow)//2-1])
	else:
		print(wow[len(wow)//2],wow[len(wow)//2])
			


		

		
	

# for i in wow_list:
# 	i = list(i)
# 	if len(i)%2 == 0:
# 		if i[-1]>i[0]:
# 			print(i[0],i[-1])
# 		else:
# 			print(i[-1],i[0])
# 	else:
# 		print(i[len(i)//2],i[len(i)//2])
