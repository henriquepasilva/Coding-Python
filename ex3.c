#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main ()
{
    float NH, CH, SB, salario_bruto;

    printf("\nIntroduza o número de horas que trabalhou este mês: ");
    scanf("%f", &NH);
    printf("\nIntroduza o custo por hora dos seus serviços: ");
    scanf("%f", &CH);
    printf("\nIntroduza o seu salário base: ");
    scanf("%f", &SB);

    salario_bruto = NH * CH + SB;

    printf("\nO seu salário bruto deste mês é %.2f euros!", salario_bruto);
}