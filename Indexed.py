n=0
m=[None]*20
i=0
j=0
sb=[None]*20
s=[None]*20
b=[[0 for i in range(20)] for j in range(20)]
x=0

print("Enter no. of files:")
n=int(input())
for i in range(0,n):
  print("Enter starting block and size of file",i+1,":")
  sb[i]=int(input())
  # s[i]=int(input()) #starting block and size of the file
  # print("Enter number of blocks occupied by file",i+1,":")
  m[i]=int(input())  #may be the no. of blocks the file is going to cover
  print("Enter blocks of file",i+1,":")
  for j in range(0,m[i]):
    b[i][j]=int(input())
print("\nFile\tindex\tlength\n")
for i in range(0,n):
  print(i+1,"\t",sb[i],"\t",m[i])
print("\nEnter file name:")
x=int(input())
print("File name is:",x)
i=x-1
print("Index is",sb[i],":")
print("Blocks occupied are:")
for j in range(0,m[i]):
  print(b[i][j],end=" ")
