# start = int(input())
# end = int(input())
# list_list = []
# for a in range(start,end+1):
# 	list_list.append(a)
# 	for i in range(2,int(a/2)+1):
# 		if a%i == 0:
# 			if a in list_list:
# 				list_list.remove(a)
# if list_list:
# 	if len(list_list) >1:
# 		if list_list[0] == 1:
# 			list_list = list_list[1:]
# 		print(sum(list_list),list_list[0],sep="\n")
# 	else:
# 		if list_list[0] != 1:
# 			print(sum(list_list),list_list[0],sep="\n")
# 		else:
# 			print(-1)
# else:
# 	print(-1)

# answer = int(input())
# answer_list = []
# for a in range(2,answer+1):
# 	answer_list.append(a)
# 	for i in range(2,int(a/2)+1):
# 		if a%i == 0:
# 			if a in answer_list:
# 				answer_list.remove(a)
# result_list = []
# count = 0
# while answer != 1:
# 	if answer >1:
# 		division = answer_list[count]
# 		if answer%division == 0:
# 			answer = answer//division
# 			result_list.append(division)
# 		else:
# 			count+=1
# 	else:
# 		break
	
# if len(result_list)>0:
# 	for a in result_list:
# 		print(a)

# answer = int(input())
# if answer >1:
# 	while answer !=1:
# 		for a in range(2,answer+1):
# 			wow = answer//a
# 			if answer%a == 0:
# 				print(a)
# 				answer = wow
# 				break #break 해버리면 a가 다음으로 넘어가지않고 계속 똑같은 a가 지속됨
# 			else:
# 				pass

answer = input().split(" ")
answer = [int(i) for i in answer]
start = answer[0]
end = answer[1]
while start != end:
	for a in range(start, end+1):
		print("a",a)
		if a%start == 0:
			start+1
		else:
			print(a,start)
			start+=1
	

		
