f=[None]*50
i=0
st=0
lent=0
j=0
c=1
k=0
count=0
for i in range(0,50):
  f[i]=0
while c==1:
  count=0
  print("\nEnter starting block and length of files:")
  st=int(input())
  lent=int(input())
  for k in range(st,(st+lent)):
    if(f[k]==0):
      count+=1
  if(lent==count):
    for j in range(st,(st+lent)):
      if(f[j]==0):
        f[j]=1
        print(j,f[j])
    if(j!=(st+lent-1)):
      print("\nThe file is allocated to disk\n")
  else:
    print("\n The file is not allocated \n")
  print("Do you want to enter more file(Yes - 1/No - 0)")
  c=int(input())
