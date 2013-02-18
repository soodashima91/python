
def push(list,x):
	list.append(x)
def pop(list):
	x=list[-1]
	del list[-1]
	return x

list=[]
push(list,1)
print pop(list)