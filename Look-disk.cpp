#include<vector>
#include<iostream> 
#include<cstdio>
#include<algorithm>
using namespace std;
 int main()
 {
   int n;
   int tracsTrav=0;
   char dir;
   printf("\nEnter the number of tracks:");
   scanf("%d",&n);
   printf("\nEnter the starting head:");
   int start;
   scanf("%d",&start);

   printf("\nEnter the direction:");
   cin>>dir;

  
   vector <int> v(n+1);
   v[0]=start;

   printf("\nEnter all the track numbers:");
   for(int i=1;i<=n;i++)
   {
     scanf("%d",&v[i]);
   }

   printf("\n\nBefore sort track=");
   for(int i=0;i<=n;i++)
   {
        printf("%d ",v[i]); 
   }

    sort(v.begin(),v.end());

    printf("\n\nAfter sort track=");
   for(int i=0;i<=n;i++)
   {
        printf("%d ",v[i]); 
   }

     

     int temp=find(v.begin(),v.end(),start)-v.begin();
    //  printf("\nElement found at:%d",temp);
    
    if(dir=='R')
    {
      for (int i=temp;i<=n;i++)
      {
        printf("\n\nTrack no=%d got executed!",v[i]);
      }

      tracsTrav+=(v[n]-v[temp]);

      tracsTrav+=(v[n]-v[0]);
      for (int i=temp-1;i>=0;i--)
      {
        printf("\n\nTrack no=%d got executed!",v[i]);
      }
    }else{
      for (int i=temp;i>=0;i--)
      {
        printf("\n\nTrack no=%d got executed!",v[i]);
      }
          tracsTrav+=(v[temp]-v[0]);
          for (int i=temp+1;i<=n;i++)
      {
        printf("\n\nTrack no=%d got executed!",v[i]);
      }
          tracsTrav+=(v[n]-v[0]);
    }

     printf("\nTotal tracks travrsed=%d",tracsTrav);
     printf("\nAverage seek Time=%f",(float)tracsTrav/n);
 }
