
answer = input().split(" ")
answer = [int(i) for i in answer]
x = answer[0]
y = answer[1]
r1 = answer[2]
a = answer[3]
b = answer[4]
r2 = answer[5]
first_x_range = list(range(x-r1,x+r1+1))
first_y_range = list(range(y-r1,y+r1+1))
second_x_range = list(range(a-r2,a+r2+1))
second_y_range = list(range(b-r2,b+r2+1))

wow = list(set(first_y_range).intersection(second_y_range))
print(wow)