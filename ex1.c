#include <stdio.h>


int ler_tamanho() {
    int n;
    do {
        printf("Digite o número de elementos (entre 1 e 20): ");
        scanf("%d", &n);
        if (n < 1 || n > 20) {
            printf("Valor inválido! Tente novamente.\n");
        }
    } while (n < 1 || n > 20);
    return n;
}


void ler_vetor(int v[], int n) {
    for (int i = 0; i < n; i++) {
        printf("Digite o valor %d: ", i + 1);
        scanf("%d", &v[i]);
    }
}


int encontrar_maior(int v[], int n) {
    int maior = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] > maior) {
            maior = v[i];
        }
    }
    return maior;
}


int encontrar_menor(int v[], int n) {
    int menor = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < menor) {
            menor = v[i];
        }
    }
    return menor;
}


int main() {
    int N = ler_tamanho(); 
    int vetor[N];          

    ler_vetor(vetor, N);   

    int maior = encontrar_maior(vetor, N);
    int menor = encontrar_menor(vetor, N);

    printf("Maior valor: %d\n", maior);
    printf("Menor valor: %d\n", menor);

    return 0;
}