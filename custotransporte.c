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
        printf("\nInsira a distânica em KM: ");
        scanf ("%d", &distancia);
        if (distancia <= 0 || distancia > 5000)
        {
            printf("\nDistância inválida. Insira um valor posito e inferior a 5000 km!");
        }
    } while (distancia <= 0 || distancia > 5000);

    do {
        printf("\nInsira o peso em KG: ");
        scanf ("%f", &peso);
        if (peso <= 0 || peso > 5000)
        {
            printf("\nPeso inválido. Insira um valor positivo e inferior a 5000 kg!");
        }
    } while (peso <= 0 || peso > 5000);

    if (peso <= 100) {
        custoEmpresaA += peso * 0.025;
    } else if (peso <= 200) {
        custoEmpresaA += 100 * 0.025 + (peso - 100) * 0.2;
    } else {
        custoEmpresaA += 100 * 0.025 + 100 * 0.02 + (peso - 200) * 0.01;
    }
    custoEmpresaA = distancia * 0.5;

    if (distancia * 0.7 < 5.5)
    {
        custoEmpresaB = 5.5;
    } else {
        custoEmpresaB = distancia * 0.7;
    }

    printf ("\nO custo do seu serviço na Empresa A é de: %.2f euros\n", custoEmpresaA);
    printf ("\nO custo do seu serviço na Empresa B é de: %.2f euros\n", custoEmpresaB);

    if (custoEmpresaA > custoEmpresaB)
    {
        printf("\nA Empresa B apresenta um custo mais vantajoso!");
    } else if (custoEmpresaA < custoEmpresaB) {
        printf("\nA Empresa A apresenta um custo mais vantajoso!");
    } else {
        printf("\nAs empresas apresentam o mesmo valor!");
    }

return 0;

}