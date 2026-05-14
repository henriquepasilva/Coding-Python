#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 int main()
{
    int x,m,b;
    float y;

    printf("Insira o X:");
    scanf("%d", &x);

    printf("Insira o M:");
    scanf("%d", &m);

    printf("Insira o B:");
    scanf("%d", &b);

    y = (m*x)+b;

    printf("a ordenada y é: %.2f", y);


}