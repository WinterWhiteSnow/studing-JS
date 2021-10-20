test_case = int(input())
answer_list = []
while len(answer_list) != test_case:
	answer = input().split()
	answer = [int(i) for i in answer]
	answer_list.append(answer)
for b in answer_list:
	start = b[0]
	end = b[1]
	wow = [start-1,start,start+1]
	count = 0
	for a in range(end):
		count +=1
		for i in range(len(wow)):
			wow[i]+=1
		if wow[-1] == end:
			if start == 0:
				print(count+1)
			else:
				print(count)	
# test_case = int(input())
# the_num = 0
# result = []
# while the_num != test_case:
# 	the_num+=1
# 	count = 0
# 	answer = input().split()
# 	answer = [int(i) for i in answer]
# 	start = answer[0]
# 	end = answer[1]
# 	wow = [start-1,start,start+1]
# 	while wow[-1] != end:
# 		for a in range(end):
# 			count +=1
# 			for i in range(len(wow)):
# 				wow[i]+=1
# 			if wow[-1] == end:
# 				break
# 	if start == 0:
# 		result.append(count+1)
# 	else:
# 		result.append(count)
# for i in result:
# 	print(i)	