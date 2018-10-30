import sys
if __name__=="__main__":
	p=int(input("Enter the number of processes:"))
	m=int(input("Enter the number of resources:"))

	temp=p

	infinite=[0]*p

	record=[1]*p
	record1=[0]*p

	resource=[0]*m
	alo = [[0] * m for i in range(p)]
	ma= [[0]*m for i in range(p)]
	need=[[0]*m for i in range(p)]
	print("Enter the available resources")
	for i in range(0,m):
		resource[i]=int(input("Enter the availability of Resource"+str(i)+":"))

	print("The availability array:"+str(resource))

	print("Enter the allocation matrix:")
	for i in range(0,p):
		for j in range(0,m):
			alo[i][j]=int(input())
	#
	#
	print("The allocation matrix="+str(alo))
	#
	print("Enter the Max matrix:")
	for i in range(0,p):
		for j in range(0,m):
			ma[i][j]=int(input())

	print("The max matrix="+str(ma))

	for i in range(0,p):
		for j in range(0,m):
			need[i][j]=ma[i][j]-alo[i][j]
			# ma[i][j]=int(input())
	print("The need matrix="+str(need))

	while temp > 0:
		infinite[temp] += 1
		if(infinite[temp]>3):
			print("Unsafe Condition!")
			sys.exit()
		for i in range(0,p):
			for j in range(0,m):
				if(need[i][j]>resource[j]):
					record[i]=0
			if (record[i]==1 and record1[i]!=1):
				temp=temp-1
				record1[i]=1
				print("Process "+str(i+1)+" got executed!")
				for k in range(0,m):
					resource[k]+=alo[i][k]
				print("New resource vector="+str(resource))
			record[i] = 1

	if temp==0:
		print("Safe Condition!")













