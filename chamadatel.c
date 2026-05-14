#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main () {
    float duracao, preco, tarifario;
    printf("A sua chamda durou: ");
    scanf("%f", &duracao);
    
    if (duracao <= 1){
        tarifario = duracao * 0.30;
        printf("Como a sua chamada foi inferior a 1 min você terá que pagar: %.2f\n", tarifario);
    }
    else if (duracao > 1 && duracao <= 5){
        tarifario = 0.30 + (duracao - 1) * 0.15;
        printf("Como a sua chamada durou entre 1 e 5 min você terá que pagar: %.2f\n", tarifario);
    }
    else if (duracao >  5){
        tarifario = 0.30 + (4 * 0.15) + (duracao - 5) * 0.08;
        printf("Como a sua chamada excedeu os 5 min, você terá de pagar: %.2f\n", tarifario);
    }
    if (duracao >= 20){
        tarifario = (0.30 + (4 * 0.15) + (duracao - 5) * 0.08) * 0.9 ;
        printf("Mas como a sua chamada excedeu os 20 minutos, você terá um desconto de 10 por cento, logo irá pagar: %.2f\n", tarifario);
    }

    return 0;
    
}