#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main ()
{
    float duracao, custo;

    printf("A sua chamada durou: ");
    scanf("%f", &duracao);

    if (duracao <= 1) {
        custo = duracao * 0.30;
        printf("\nComo a sua chamada durou menos de um minuto você irá pagar %.2f euros!", custo);
    } else if (duracao > 1 && duracao <= 5) {
        custo = 0.30 + (duracao - 1) * 0.15;
        printf("\nComo a sua chamada durou entre 1 a 5 minutos você irá pagar %.2f euros!", custo);
    } else if (duracao > 5 && duracao < 20) {
        custo = 0.30 + (4*0.15) + (duracao - 5) * 0.08;
        printf("\nComo a sua chamada durou mais de 5 minutos você irá pagar %.2f euros!", custo);
    }
    if (duracao >= 20) {
        custo = (0.30 + (4*0.15) + (duracao - 5) * 0.08) * 0.09;
        printf("\nComo a sua chamada execeu os 20 minutos você irá pagar %.2f euros! Mas irá usufruir de um desconto de 10 por cento.", custo);
    }
    
    return 0;
}