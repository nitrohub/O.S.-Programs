#include<algorithm>
#include<vector>
#include<iostream>
#include<cstdio>
#include<cstdlib>
 using namespace std;
  int main()
  {
    int n;
    int tracsTrav=0;
    int flag1=0;
    int flag2=0;
    printf("\nEnter the number of tracks to be traversed:");
    scanf("%d",&n);
    int temp=n+1;
    vector <int> v(n+1);
    printf("\nEnter the starting track:");
    int start;
    scanf("%d",&start);
    v[0]=start;
    printf("\nEnter the tracks\n");
    for(int i=1;i<n+1;i++)
          scanf("%d",&v[i]);
 
     printf("\nEntered tracks=");

     for(int i=1;i<n+1;i++)
          printf("%d ",v[i]);
    


     sort(v.begin(),v.end());

     printf("\nAfter sort:");

     for(int i=0;i<n+1;i++)
          printf("%d ",v[i]);
      
        int i=(find(v.begin(),v.end(),start)-v.begin());
        // i--;
        printf("\nValue of i=%d",i);

      int temp1=i;
      int temp2=i-1;
      int temp3=i+1;
      int temp4=0;
      int temp5=0;


     while(temp!=0)
     {
        printf("\nValue of temp=%d",temp);
        printf("\nValue of temp2=%d",temp2);
        printf("\nValue of temp3=%d",temp3);
        printf("\n Value of tracTrav=%d",tracsTrav);
       if(temp2!=-1)
       {
          temp4=abs(v[temp1]-v[temp2]);
       }else{
         
         flag1=1;
         temp1=temp3;
         tracsTrav+=abs(v[temp2+1]-v[temp3]);
         goto l1;

       }
       if(temp3!=n)
       {
        temp5=abs(v[temp1]-v[temp3]);
       }else{ 
          
          temp1=temp2;
          tracsTrav+=abs(v[temp3-1]-v[temp1]);
          flag2=1;
          goto l2;

            }
      if(temp4<temp5)
      {
        tracsTrav+=temp4;
        temp1=temp2;
        temp2--;
        temp--;
      }else{
        tracsTrav+=temp5;
        temp1=temp3;
        temp3++;
        temp--;
      }
     }

    l1:  if(flag1==1)
     {
        tracsTrav+=v[n]-v[temp1];
        printf("\nValue of tracTrav=%d",tracsTrav);
     }
       l2:  if(flag2==1)
     {
    tracsTrav+=v[0]-v[temp1];
    printf("\nValue of tracTrav=%d",tracsTrav);
     }

     printf("\nTracks traversed=%f",(float)tracsTrav/n);
  }