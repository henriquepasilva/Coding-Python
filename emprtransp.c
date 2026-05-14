// Henrique Silva a22211081

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main ()
{
    int distancia = 0;
    float peso = 0.0;
    float custoEmpresaA = 0.0;
    float custoEmpresaB = 0.0;

    do {
        printf("Insira a distancia em km: ");
        scanf("%d", &distancia);
        if (distancia <= 0 || distancia > 5000) {
            printf("\nDistância inválida! Tente novamente, mas desta vez com um número inteiro positivo e inferior a 5000km!\n");
        }
    } while (distancia <= 0 || distancia > 5000);
    
    do {
         printf("\nInsira o peso em kg: ");
        scanf("%f", &peso);
        if (peso <= 0 || peso > 5000) {
            printf("\nPeso inválido! Tente novamente, mas desta vez com um número inteiro positivo e inferior a 5000kg!\n");
        }
    }  while (peso <= 0 || peso > 5000);

    if (peso <= 100) {
        custoEmpresaA += peso * 0.025;
    } else if (peso <= 200) {
        custoEmpresaA += 100 * 0.025 + (peso - 100) * 0.02;
    } else {
        custoEmpresaA += 100 * 0.025 + 100 * 0.02 + (peso - 200) * 0.01;
    }
    custoEmpresaA += distancia * 0.5;

    if (distancia * 0.7 < 5.5) {
        custoEmpresaB = 5.5;
    } else {
        custoEmpresaB = distancia * 0.7;
    }

    printf("\nO custo da Empresa A vai ser de: %.2f euros\n", custoEmpresaA);
    printf("\nO custo da Empresa B vai ser de: %.2f euros\n", custoEmpresaB);

    if (custoEmpresaA < custoEmpresaB) {
        printf("\nA Empresa A apresenta um custo mais vantajoso!");
    } else if (custoEmpresaA > custoEmpresaB) {
        printf("\nA Empresa B apresenta um custo mais vantajoso!");
    } else {
        printf("\nAmbas apresentam o mesmo valor, vá pela sua preferência!");
    }

}