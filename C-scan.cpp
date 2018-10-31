#include<vector>
#include<iostream> 
#include<cstdio>
#include<algorithm>
using namespace std;
 int main()
 {
   int n;
   int tracsTrav=0;
   printf("\nEnter the number of tracks:");
   scanf("%d",&n);
   printf("\nEnter the starting head:");
   int start;
   scanf("%d",&start);
  
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
    
    if(temp!=n&&temp!=0)
    {
      for(int i=temp;i<=n;i++)
      {
        printf("\n\nTrack=%d got executed!\n",v[i]);
      }
      printf("\nHead is on track 199\n");
      tracsTrav+=(199-v[temp]);
      printf("\nHead is on track 0\n");
      tracsTrav+=(199-0);
      for(int i=0;i<temp;i++)
      {
        printf("\nTrack no=%d got executed!\n",v[i]);
      }
      tracsTrav+=(v[temp-1]-0);
    }else if(temp==n)
    {
       printf("\nHead is on track 199\n");
       tracsTrav+=(199-0);  //199->0
       printf("\nHead is on track 0\n");
      tracsTrav+=(v[temp-1]-0);  //0->lastrequest
      for(int i=0;i<temp;i++)
      {
        printf("\nTrack=%d got executed!\n",v[i]);
      }
    }else if(temp==0){
      tracsTrav+=(v[n]-0);  //0->last element
      for(int i=0;i<=n;i++)
      {
        printf("\nTrack=%d got executed!",v[i]);
      }
    }

     printf("\nTotal tracks travrsed=%d",tracsTrav);
     printf("\nAverage seek Time=%f",(float)tracsTrav/n);
 }
