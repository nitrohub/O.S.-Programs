#include <vector>
#include<iostream> 
#include<cstdio>
#include<cstdlib>
using namespace std;
 int main()
 {
   int n;
   int tracsTrav=0;
   int start;
   printf("\nEnter the number of processes:");
   scanf("%d",&n);
   vector <int> v(n);
  //  v.push_back(10);
  // printf("%d",v[5]);
   printf("\nEnter the starting track:");
   scanf("%d",&start);
   printf("\nEnter the processes:");
 
    scanf("%d",&v[0]);
    tracsTrav+=abs(start-v[0]);

   for(int i=1;i<n;i++)
   {
      scanf("%d",&v[i]);
      tracsTrav+=abs(v[i]-v[i-1]);
   }

    printf("\nThe processes are:");
    for(int i=0;i<n;i++)
   {
     printf("%d ",v[i]);
   }

   printf("\nTotal number of tracks traversed=%d",tracsTrav);
   printf("\nThe average seek time=%f",((float)tracsTrav/n));

  //  ?  v[1]=10;
  //  printf("%d",v[1]);
 }