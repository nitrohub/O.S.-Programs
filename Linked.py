f=[None]*50
p=0
i=0
st=0
lent=0
j=0
c=1
k=0
a=0

for i in range(0,50):
  f[i]=0
print("\nEnter how many blocks already allocated:")
p=int(input())
if(p!=0):
  print("\nEnter blocks already allocated:")
for i in range(0,p):
  a=int(input())
  f[a]=1
while c==1:
  print("Enter index starting block and length: ")
  st=int(input())
  lent=int(input())
  k=lent
  if(f[st]==0):
    for j in range(st,(st+k)):
      if(f[j]==0):
        f[j]=1
        print(str(j),"Allocated")
      else:
        print(str(j),"Block is already allocated \n")
        k+=1
  else:
    print(str(st),"starting block is already allocated \n")
  print("Do you want to enter more file(Yes - 1/No - 0)?")
  c=int(input())
