#include<stdio.h>
#include<stdlib.h>

int *temp=NULL;

int func(int *a,int n,int m)
{
	int i=0;
	if(temp[n]==-1){
   for(i=0;i<m;i++)
   {
   	if(n>=a[i])
   	{
   		if(temp[n-a[i]]!=-1)
   			temp[n]+=temp[n-a[i]];
   		else {
   			int k=func(a,n-a[i],m);
   		     if(k!=-1)
   		     	temp[n]+=k;
   		 }
   	}
   }
   return temp[n];
}
 else 
 	return temp[n];
}

int main()
{
int n,m;
scanf("%d %d",&n,&m);
int *a=(int*)malloc(m*sizeof(int));
temp=(int*)malloc((n+1)*sizeof(int));
int i=0;
for(i=0;i<=n;i++)
	temp[i]=-1;
temp[0]=1;
for(i=0;i<m;i++)
scanf("%d",&a[i]);
int ans = func(a,n,m);
printf("%d\n",ans);
return 0;
}
