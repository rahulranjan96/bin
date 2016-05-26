#include<stdio.h>
#include<stdlib.h>

typedef struct 
{
	int condition;
	int x;
	int y;
}joint;

typedef struct{
  float value;
  int i;
  int j;
}std_matrix;

int main()
{
 int num_joint,i=0,ei=0,j=0,k=0,degree=0;
 printf("Enter number of joints:");
 scanf("%d",&num_joint);
 int *len=(int*)malloc((num_joint-1)*sizeof(int));
 joint *array=(joint*)malloc(num_joint*sizeof(joint));
 printf("Enter Lengths\n");
 for(i=0;i<num_joint-1;i++)
 {
 	printf("Enter %dth length:",i+1);
 	scanf("%d",&len[i]);
 }
printf("Enter the value (ei):");
scanf("%d",&ei);
for(i=0;i<num_joint;i++)
{
	printf("0:Fixed\n1:Roller\n2:Free\nEnter Choice: ");
	scanf("%d",&array[i].condition);
}
//printf("\n\n\nTill here OKAY!!!\n\n\n");
array[0].x=0;
array[0].y=0;
j++;
for(i=0;i<num_joint;i++)
{
	if(array[i].condition!=0)
	{
	array[i].x=j;
	j++;
	array[i].y=j;
	j++;
    }
}
//printf("\n\n\nTill here OKAY!!!\n\n\n");
degree=j-1;

std_matrix **array1 = (std_matrix**)malloc((num_joint-1)*sizeof(std_matrix*));
//printf("\n\n\nTill here OKAY!!!\n\n\n");
for(i=0;i<num_joint-1;i++)
array1[i]=(std_matrix*)malloc(16*sizeof(std_matrix));
//printf("\n\n\nTill here OKAY!!!\n\n\n");
for(i=0;i<num_joint-1;i++)
{
	array1[i][0].value = (float)(12*ei)/(len[i]*len[i]*len[i]);
	array1[i][1].value = (float)(6*ei)/(len[i]*len[i]);
	array1[i][2].value = (float)(-12*ei)/(len[i]*len[i]*len[i]);
	array1[i][3].value = (float)(6*ei)/(len[i]*len[i]);
	array1[i][4].value = (float)(6*ei)/(len[i]*len[i]); 
	array1[i][5].value = (float)(4*ei)/(len[i]);
	array1[i][6].value = (float)(-6*ei)/(len[i]*len[i]);
	array1[i][7].value = (float)(2*ei)/(len[i]);
	array1[i][8].value = (float)(-12*ei)/(len[i]*len[i]*len[i]);
	array1[i][9].value = (float)(-6*ei)/(len[i]*len[i]);
	array1[i][10].value = (float)(12*ei)/(len[i]*len[i]*len[i]);
	array1[i][11].value = (float)(-6*ei)/(len[i]*len[i]);
	array1[i][12].value = (float)(6*ei)/(len[i]*len[i]);
	array1[i][13].value = (float)(2*ei)/(len[i]);
	array1[i][14].value = (float)(-6*ei)/(len[i]*len[i]);
	array1[i][15].value = (float)(4*ei)/(len[i]);
	array1[i][0].i=array[i].x;
	array1[i][0].j=array[i].x;
	array1[i][1].i=array[i].x;
	array1[i][1].j=array[i].y;
	array1[i][2].i=array[i].x;
	array1[i][2].j=array[i+1].x;
	array1[i][3].i=array[i].x;
	array1[i][3].j=array[i+1].y;
	array1[i][4].i=array[i].y;
	array1[i][4].j=array[i].x;
	array1[i][5].i=array[i].y;
	array1[i][5].j=array[i].y;
	array1[i][6].i=array[i].y;
	array1[i][6].j=array[i+1].x;
	array1[i][7].i=array[i].y;
	array1[i][7].j=array[i+1].y;
	array1[i][8].i=array[i+1].x;
	array1[i][8].j=array[i].x;
	array1[i][9].i=array[i+1].x;
	array1[i][9].j=array[i].y;
	array1[i][10].i=array[i+1].x;
	array1[i][10].j=array[i+1].x;
	array1[i][11].i=array[i+1].x;
	array1[i][11].j=array[i+1].y;
	array1[i][12].i=array[i+1].y;
	array1[i][12].j=array[i].x;
	array1[i][13].i=array[i+1].y;
	array1[i][13].j=array[i].y;
	array1[i][14].i=array[i+1].y;
	array1[i][14].j=array[i+1].x;
	array1[i][15].i=array[i+1].y;
	array1[i][15].j=array[i+1].y;

}
//printf("\n\n\nTill here OKAY!!!\n\n\n");

float ***k_array=(float***)malloc((num_joint-1)*sizeof(float**));
//printf("\n\n\nTill here OKAY!!!\n\n\n");
for(i=0;i<num_joint-1;i++)
k_array[i]=(float**)malloc(degree*sizeof(float*));
//printf("\n\n\nTill here OKAY!!!\n\n\n");
for(i=0;i<num_joint-1;i++)
for(j=0;j<degree;j++)
	k_array[i][j]=(float*)malloc(degree*sizeof(float));
//printf("\n\n\nTill here OKAY!!!\n\n\n");
for(k=0;k<num_joint-1;k++)
	for(i=0;i<degree;i++)
		for(j=0;j<degree;j++)
		{
			k_array[k][i][j]=0;
		}
//printf("\n\n\nTill here OKAY!!!\n\n\n");
for(k=0;k<num_joint-1;k++)
	for(i=0;i<16;i++)
	{
		k_array[k][array1[k][i].i-1][array1[k][i].j-1]=array1[k][i].value;
	}
//printf("\n\n\nTill here OKAY!!!\n\n\n");
float **final=(float**)malloc(degree*sizeof(float*));
for(i=0;i<degree;i++)
 final[i]=(float*)malloc(degree*sizeof(float));
for(i=0;i<degree;i++)
	for(j=0;j<degree;j++)
		final[i][j]=0;
for(i=0;i<degree;i++)
	for(j=0;j<degree;j++)
		for(k=0;k<num_joint-1;k++)
		{
			final[i][j]+=k_array[k][i][j];
		}
for(i=0;i<degree;i++)
{  printf("\n");
	for(j=0;j<degree;j++)
		printf("%f ",final[i][j]);
}
printf("\n");
 return 0;
}

