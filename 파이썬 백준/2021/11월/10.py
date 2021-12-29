# answer_list = []
# while True:
#   a = input()
#   if a == "0":
#       break
#   else:
#     if a == a[::-1]:
#       answer_list.append("yes")    
#     else:
#       answer_list.append("no")
# for i in answer_list:
#   print(i)

a = input()
a_int = int(a)
a_list = []
while a_int !=0:
    wow= len(str(a_int))-1   
    maxi = (10**(wow))+1
    b = a_int//maxi
    test = a_int-maxi*b
    
    a_int = a_int-maxi*b 
    a_list.append(b)
print(a_list)
#216
# 101 2 14
# 11 1 3
# 2 1 1