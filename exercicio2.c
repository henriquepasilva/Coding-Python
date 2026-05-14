#include <stdio.h>

int main() {
    int n = 20;  
    int i = 0;   
    double soma = 0.0;

    printf("Série: ");

    while (i < n) {
        double termo = 1.0 / (2 * i + 1);

        if (i % 2 != 0) {  
            termo *= -1;
        }

        soma += termo;

    
        if (i == 0) {
            printf("%.2f ", termo);
        } else {
            printf("%+ .2f ", termo);
        }

        i++; 
    }

    printf("\nSoma dos 20 termos: %.6f\n", soma);
    return 0;
}