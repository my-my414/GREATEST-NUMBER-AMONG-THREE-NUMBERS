#include<stdio.h>
int main()
{
    int a,b,c;
    printf("Enter a number :");
    scanf("%d%d%d",&a,&b,&c);
    if (a>b && a>c)
    {
        printf("A is greater");
    
    }
    else if(b>a && b>c)
    {
        printf("B is graeter");
    }
    else
    {
        printf("c is greater");
    }
    

}
