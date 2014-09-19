
def solve(items,size):
	v=[[0 for i in range(size+1)] for j in range(len(items)+1)]
	keep=[[0 for i in range(size+1)] for j in range(len(items)+1)]
	for i in range(size+1):
		v[0][i]=0
	for i in range(0,len(items)):
		for currentsize in range(1,size+1):
			itemweight=items[i][0]
			itemvalue=items[i][1]
			itemindex=i+1
			if itemweight<=currentsize:
				remainingweight=currentsize-itemweight
				if v[itemindex-1][remainingweight]+itemvalue > v[itemindex-1][currentsize]:
					v[itemindex][currentsize]=v[itemindex-1][remainingweight]+itemvalue
					keep[itemindex][currentsize]=1
				else:
					v[itemindex][currentsize]=v[itemindex-1][currentsize]
			else:
				v[i][currentsize]=0
	spaceleft=size
	itemindex=len(items)
	while spaceleft>0 and itemindex>0:
		if keep[itemindex][spaceleft]==1:
			print items[itemindex-1]
			spaceleft=spaceleft-items[itemindex-1][0]
			itemindex=itemindex-1
		else:
			itemindex=itemindex-1

	print v
	print keep
weights=[3,2,1,3,2,1]
values=[5,3,4,5,3,4]
solve(zip(weights,values),15)