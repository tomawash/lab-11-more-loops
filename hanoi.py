def hanoi(n, f, h, t):
	if n==0:
		pass
	else:
		hanoi(n-1, f, t, h)
		print("Move disk from " + f + " to " + t)
		hanoi(n-1,h,f,t)

hanoi(4,"A","B","C")