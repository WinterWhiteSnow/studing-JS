# answer_list = []

# while True:
# 	answer = int(input())
# 	if answer == 0 :
# 		break
# 	start = answer
# 	end = 2*answer
# 	count = 0
# 	list_list = {}
# 	for i in range(2,end+1):
# 		if i not in list_list:
# 			for a in range(i,end+1,i):
# 				list_list[a]=1
# 			list_list[i]=0


# 	for key,value in list_list.items():
# 		if key > start and value == 0:
# 			count+=1
# 	answer_list.append(count)

# for i in answer_list:
# 	print(i)




answer = 123456
start = answer
end = 2*answer
list_list = {}
for i in range(2,end+1):
	if i not in list_list:
		for a in range(i,end+1,i):
			list_list[a]=1
		list_list[i]=0

answer_list = []

while True:
	wow = int(input())
	wow2 = wow*2
	count = 0
	if wow ==0:
		break
	for key,value in list_list.items():
		if wow2 >= key > wow and value == 0:
			count+=1
	answer_list.append(count)
	
for i in answer_list:
	print(i)