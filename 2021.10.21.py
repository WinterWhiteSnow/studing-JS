test_case = int(input())
answer_list = []
while len(answer_list) != test_case:
	answer = input().split(" ")
	answer = [int(i) for i in answer]
	if answer[1] > answer[0]:
		answer_list.append(answer[1]- answer[0])
result_list = []
for c in answer_list:
	distance = c
	if distance <= 2 :
		result_list.append(distance)
	else:
		move = 3
		count = 0
		for i in range(3,distance+1):
			call = 4
			count+=1
			if i == distance:
				result_list.append(move)
			else:
				if count == int(call/2):
					move+=1
				elif count == call:
					move+=1
					count =0
					call+=2

for a in result_list:
	print(a)	
# result_list = []
# distance = 5
# move = 3
# two = 2
# count =0
# for i in range(3,distance+1):
# 	call = two*2
# 	count+=1
# 	print(move)
# 	if count == int(call/2):
# 		move+=1
# 	elif count == call:
# 		move+=1
# 		count =0
# 		two+=1

# print(result_list)


			