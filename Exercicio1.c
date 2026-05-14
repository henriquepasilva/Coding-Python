#include <stdio.h>

int ler_inteiro_par(int *valor) {
    int num;
    do {
        printf("Insira um número par (não zero): ");
        scanf("%d", &num);
        if (num == 0) return 1;
    } while (num % 2 != 0);

    *valor = num;
    return 0;
}

int main() {
    int soma = 0, valor, resultado;
    for (int i = 0; i < 4; i++) {
        resultado = ler_inteiro_par(&valor);
        if (resultado == 1) break;
        soma += valor;
    }
    printf("Soma dos pares inseridos: %d\n\n", soma);
}