# import sys

# list_list = {}
# for i in range(2,10000+1):
# 	if i not in list_list:
# 		for a in range(i,10000+1,i):
# 			list_list[a]=1
# 		list_list[i]=0

# result_list = {}
# for key,value in list_list.items():
# 	if value == 0:
# 		result_list[key] = value
# answer_sort = sorted(result_list.keys())

# the_num = int(sys.stdin.readline())

# count =0
# answer_list = []
# while count != the_num:
# 	count +=1
# 	answer = int(sys.stdin.readline())
# 	answer_list.append(answer)

# for a in answer_list:
# 	half = a//2
# 	while half not in answer_sort or a-half not in answer_sort:
# 		half-=1
# 	print(half,a-half)

# answer = input().split(" ")
# answer = [int(i) for i in answer]
# start_x = answer[0]
# start_y = answer[1]
# end_x = answer[2]
# end_y = answer[3]
# distance_x = end_x - start_x
# distance_y = end_y - start_y
# wow = [start_x,distance_x,start_y,distance_y]
# wow.sort()
# print(wow[0])

# the_num = 3
# count = 0
# x = []
# y = []
# while count != the_num:
# 	count+=1
# 	answer =input().split(" ")
# 	answer = [int(i) for i in answer]
# 	x.append(answer[0])
# 	y.append(answer[1])
# result = {}
# for a,b in zip(x,y):
# 	if x.count(a) != 2 :
# 		result["x"] = a
# 	elif y.count(b) != 2:
# 		result["y"] = b
	
# print(result["x"],result["y"])


# answer_list = []
# while True:
# 	answer = input().split(" ")
# 	answer = [int(i) for i in answer]
# 	answer.sort()
# 	if answer[0] == 0:
# 		break
# 	else:
# 		if answer[0]**2+answer[1]**2 == answer[2]**2:
# 			answer_list.append("right")
# 		else:
# 			answer_list.append("wrong")
# for i in answer_list:
# 	print(i)

# import math
# r = int(input())
# one = (math.pi)*(r*r)
# two = (2*r)*r
# print(f"{one:.6f}")
# print(f"{two:.6f}")

# the_num = int(input())
# count = 0
# answer_list = []
# while count != the_num:
# 	count+=1
# 	answer = input().split(" ")
# 	answer = [int(i) for i in answer]
# 	x = answer[0]
# 	y = answer[1]
# 	r1 = answer[2]
# 	a = answer[3]
# 	b = answer[4]
# 	r2 = answer[5]
# 	distance_x = a-x
# 	distance_y = b-y
# 	if distance_x == distance_y:
# 		if r1 == r2:
# 			answer_list.append(-1)
# 		else:
# 			answer_list.append(0)
# 	elif distance_x == 0 or distance_y == 0:
# 		if r1+r2 == abs(distance_x) or r1+r2 == abs(distance_y):
# 			answer_list.append(1)
# 		elif r1+r2 > distance_x or r1+r2 > distance_y:
# 			answer_list.append(2)
# 		else:
# 			answer_list.append(0)
# 	else:
# 		answer_list.append(2)
# for i in answer_list:
# 	print(i)

answer = [0,0,1,0,1,5]
x = answer[0]
y = answer[1]
r1 = answer[2]
a = answer[3]
b = answer[4]
r2 = answer[5]
write = (X-x)**2+
