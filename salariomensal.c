#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() 
{
    int sb;
    double gh,salario=0;
    unsigned int nh; //so deixa nh ter numeros positivos

    printf("\nQuantas horas trabalhou?");
    scanf("%d", &nh);

    printf("\nQuanto ganha por hora?");
    scanf("%lf", &gh);

    printf("\nQual é o salario base?");
    scanf("%d", &sb);

    salario=(nh*gh)+sb;

    printf("\no salario mensal bruto é: %.2f", salario);
}