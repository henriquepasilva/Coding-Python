#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {

    float a, b, c;
    float delta, equacao, equacao1;
    
    printf("Insira o valor para A: ");
    scanf("%f", &a);
    printf("Insira o valor para B: ");
    scanf("%f", &b);
    printf("Insira o valor para C: ");
    scanf("%f", &c);

    delta = b * b - 4 * a * c;

    if (a == 0) {
        printf("A equação apresentada e impossível.\n");
    } else if (delta < 0) {
        printf("A equação nao possui raízes reais.\n");
    } else {
        printf("A equação possui raízes reais.\n");

        equacao = (-b + sqrt(delta)) / (2 * a);
        equacao1 = (-b - sqrt(delta)) / (2 * a);

        printf("O valor das raízes da equação de segundo grau são: %f e %f\n", equacao, equacao1);
    }

    return 0;
}