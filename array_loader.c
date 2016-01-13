#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()

{
char line[512];
double *a1, *a2, *a3, *a4, *a5, *a6, *a7, *a8, *a9;
int n;
n = 10;
int i;
/*char line[n];*/
FILE *inp;
int m;
m = 0;
inp = fopen("MyTable_rahul.poruri.csv","r");

a1 = (double *)malloc(n*sizeof(double));
a2 = (double *)malloc(n*sizeof(double));
a3 = (double *)malloc(n*sizeof(double));
a4 = (double *)malloc(n*sizeof(double));
a5 = (double *)malloc(n*sizeof(double));
a6 = (double *)malloc(n*sizeof(double));
a7 = (double *)malloc(n*sizeof(double));
a8 = (double *)malloc(n*sizeof(double));
a9 = (double *)malloc(n*sizeof(double));
/*
fgets(line, sizeof(line), inp);
while((fgets(line, sizeof(line),inp))!=NULL)
	{
	sscanf(line,"%lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf",&a1[m],&a2[m],&a3[m],&a4[m],&a5[m],&a6[m],&a7[m],&a8[m],&a9[m]);
	m++;
	}
*/

for (i = 0; i<10; i++)
	{
	fscanf(inp,"%lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf",&a1[i],&a2[i],&a3[i],&a4[i],&a5[i],&a6[i],&a7[i],&a8[i],&a9[i]);
	}

for (i=0;i<10;i++)
	{
	printf ("%lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf,\n",a1[i],a2[i],a3[i],a4[i],a5[i],a6[i],a7[i],a8[i],a9[i]);
	}

return;
}


