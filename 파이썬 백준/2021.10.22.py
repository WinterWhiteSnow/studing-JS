# test_case = int(input())
# answer_list = []
# while len(answer_list) != test_case:
# 	answer = input().split(" ")
# 	answer = [int(i) for i in answer]
# 	if answer[1] > answer[0]:
# 		answer_list.append(answer[1]- answer[0])
# for c in answer_list:
# 	distance = c
# 	if distance <= 2 :
# 		print(distance)
# 	else:
# 		count = 0
# 		the_num = 1
# 		move = 0
# 		while distance >0:
# 			move +=1
# 			count +=1
# 			distance-=the_num
# 			if count ==2:
# 				count =0
# 				if distance > 0:
# 					the_num+=1
# 				else:
# 					pass
# 		print(move)

# test_case = int(input())
# answer_list = []
# while len(answer_list) != test_case:
# 	answer = input().split(" ")
# 	answer = [int(i) for i in answer]
# 	if answer[1] > answer[0]:
# 		answer_list.append(answer[1]- answer[0])
# for c in answer_list:
# 	distance = c
# 	count = 0
# 	the_num = 1
# 	move = 0
# 	while distance >0:
# 		move +=1
# 		count +=1
# 		distance-=the_num
# 		if count ==2:
# 			count =0
# 			if distance > 0:
# 				the_num+=1
# 			else:
# 				pass
# 	print(move)

#1 2 5 10 9

# import sys
# test_case = int(sys.stdin.readline())
# answer = input().split(" ")
# if len(answer) == test_case:
# 	answer = [int(i) for i in answer]
# 	answer.sort()
# 	if answer[0] == 1:
# 		answer = answer[1:]
# 	answer_list=[]
# 	for a in answer:
# 		for i in range(2,a):
# 			if a%i == 0:
# 				if a not in answer_list:
# 					answer_list.append(a)
# 	answer = list(set(answer).difference(answer_list))
# 	print(len(answer))

mini = int(input())
maxi = int(input())
first_list = []
answer_list=[]
for a in range(mini,maxi+1):
	first_list.append(a)
	for i in range(2,int(a/2+1)):
		if a%i == 0:
			if a not in answer_list:
				answer_list.append(a)
wow = list(set(first_list).difference(answer_list))
if wow:
	wow.sort()
	print(sum(wow))
	print(wow[0])
else:
	print(-1)
