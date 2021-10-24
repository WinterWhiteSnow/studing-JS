test_case = int(input())
answer_list = []
while len(answer_list) != test_case:
	answer = input().split()
	answer = [int(i) for i in answer]
	if answer[0] < answer[1]:
		answer_list.append(answer)
for b in answer_list:
	start = b[0]
	end = b[1]
	distance = end - start
	while distance != 1:
		if start == 0:
			distance -=1

# test_case = int(input())
# answer_list = []
# while len(answer_list) != test_case:
# 	answer = input().split()
# 	answer = [int(i) for i in answer]
# 	if answer[0] < answer[1]:
# 		answer_list.append(answer)
# for b in answer_list:
# 	start = b[0]
# 	end = b[1]
# 	wow = [start-1,start,start+1]
# 	count = 0
# 	for a in range(end):
# 		count +=1
# 		for i in range(len(wow)):
# 			wow[i]+=1
# 		if wow[-1] == end-1:
# 			if start == 0:
# 				print(count+2)
# 			else:
# 				print(count+1)

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

# test_case = int(input())
# answer_list = []
# while len(answer_list) != test_case:
# 	answer = input().split()
# 	answer = [int(i) for i in answer]
# 	if answer[0] < answer[1]:
# 		answer_list.append(answer)

# def bow(start,end,lalala):
# 	lalala+=1
# 	end = end		
# 	wow = [start-1,start,start+1]
# 	if end-1 not in wow:
# 		start = wow[-1]
# 		bow(start,end,lalala)
# 	else:
# 		if b[0] == 0:
# 			print(lalala+1)
# 		else:
# 			print(lalala)

# for b in answer_list:
# 	start = b[0]
# 	end = b[1]
# 	lalala = 0
# 	bow(start,end,lalala)


