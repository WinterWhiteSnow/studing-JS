# answer = int(input())
# count = 0
# total = 0
# num = 0
# while True:
# 	num += 1
# 	count+=num
# 	if count >= answer:
# 		total = num+1
# 		break
# wow = count-answer+1 
# dd = total-wow
# if total % 2 == 0 : 
# 	print(f"{wow}/{dd}")
# else:
# 	print(f"{dd}/{wow}")	

# import sys
# answer = sys.stdin.readline().split(" ")
# answer = [int(i) for i in answer]
# incre = answer[0]
# decre = answer[1]
# height = answer[2] - incre
# progress = 0
# days=(height/(incre-decre))+1
# if days == round(days):
# 	print(int(days))
# else:
# 	print(int(days)+1)

import sys
the_num = int(sys.stdin.readline())
answer_list = []
while len(answer_list) != the_num:
	answer = sys.stdin.readline().split(" ")
	answer = [int(i) for i in answer]
	answer_list.append(answer)

for i in answer_list:
	H = i[0]
	W = i[1]
	C = i[2]
	print(H,W,C) 
	#호텔은 101 201 301 ......H01호순으로 가고 그 후 102 202...순으로 채워짐