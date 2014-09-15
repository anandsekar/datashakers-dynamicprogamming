# n - number of steps
# k - number of steps one can take

def solve(n,possiblesteps,solutionstore):
	possibleways=0
	for step in possiblesteps:
		prev=n-step
		if prev>0:
			prevpossibleways=solutionstore[prev]
			if prevpossibleways !=-1:
				possibleways=possibleways+prevpossibleways
			else:
				prevpossibleways=solve(prev,possiblesteps,solutionstore)
				solutionstore[prev]=prevpossibleways
				possibleways=possibleways+prevpossibleways
		elif prev==0:
			possibleways=possibleways+1
	return possibleways

n=10
solutionstore=[-1] * n
print solve(n,[1,5],solutionstore)
print solutionstore
