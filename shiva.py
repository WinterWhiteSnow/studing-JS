# lis=[1,0,1]
# for i, ele in enumerate(lis) :
# 	if ele == 1:
# 		print(i)

# wow = "820578226"
# list_list= []
# for i in wow:
# 	list_list.append(i)
# num_list = [int(i) for i in list_list]
# apple = {"1":[],"2":[]}

# for count,value in enumerate(num_list):
# 	if value==0:
# 		a = count
# 	if value==1:
# 		b = count
# 	if value==2:
# 		apple["2"].append(count)
# print(apple)
	# if value==3:
	# 	print(count)
	# if value==4:
	# 	print(count)
	# if value==5:
	# 	print(count)
	# if value==6:
	# 	print(count)
	# if value==7:
	# 	print(count)
wow = [1,4,5,6,7,8]
a = "8457474524"
b = ['o', 'o', 'o', 'oo']
count_o = []
result = []
for i in b:
	count_o.append(len(i))
print(count_o)	
count = 0
for i in count_o:
	if i>=2:
		for a in range(i+1):
			count+=a
			print("a",a)
	else:
		count+=1
print(count)				
# for i in range(2+1):
# 	print(i)