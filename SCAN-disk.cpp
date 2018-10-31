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
   printf("\nEnter the direction of head:(L/R)?");
     char dir;
     cin>>dir;
     printf("Direction=%c",dir);
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
         for(int i=temp;i<=n;i++)
         {
           printf("\n\nTrack=%d got executed!\n",v[i]);
         }
         printf("\n\nHead is on track 199!");
         tracsTrav+=(199-v[temp]); //Last track 199(Since it is scan)
         if(temp!=0)
                {
                tracsTrav+=(199-v[0]);
                for(int i=temp-1;i>=0;i--)
                {
                  printf("\n\nTrack=%d got executed!\n",v[i]);
                }
                }
     }else{
       for(int i=temp;i>=0;i--)
         {
           printf("\n\nTrack=%d got executed!\n",v[i]);
         }
           printf("\n\nHead is on track no 0");
            tracsTrav+=(v[temp]-0);
            if(temp!=n){
                tracsTrav+=(v[n]-0);
                      for(int i=temp+1;i<=n;i++)
                {
                  printf("\n\nTrack=%d got executed!\n",v[i]);
                }
                        }
     }

     printf("\nTotal tracks travrsed=%d",tracsTrav);
     printf("\nAverage seek Time=%f",(float)tracsTrav/n);
 }
