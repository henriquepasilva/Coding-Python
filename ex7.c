#include <stdio.h>

int main ()
{
    float celsius, resultado;
    char unidade;

    printf("Insira a temperatura em graus Celsius (ºC) : ");
    scanf("%f", &celsius);

    printf("Diga qual a unidade de destino (K/k para Kelvin ou F/f para Fahrenheit) : ");
    scanf(" %c", &unidade);

    switch (unidade)
    {
    case 'K':
    case 'k':
        resultado = celsius + 273;
        printf("\nTemperatura em Kelvin: %.2f K\n", resultado);
        break;
    
    case 'F':
    case 'f':
        resultado = (9/5) * celsius + 32;
        printf("\nTemperatura em Fahreinheit: %.2f F\n", resultado);
        break;

    default:
        printf("\nUnidade inválida! Use somente 'K' ou 'F.\n");
    }

    return 0;
}