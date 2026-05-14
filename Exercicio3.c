#include <stdio.h>

void print_vector(int v[], int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", v[i]);
        if (i < size - 1) printf(" ");
    }
    printf("]");
}

int count_vector(int v[], int size, int value) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (v[i] == value) count++;
    }
    return count;
}

int uniq_vector(int origem[], int destino[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (count_vector(origem, size, origem[i]) == 1) {
            destino[count] = origem[i];
            count++;
        }
    }
    return count;
}

int main() {
    int vec1[10] = {2, 4, 4, 10, 8, 8, 4, 7, 9, 10};
    int vec2[10];
    int count = uniq_vector(vec1, vec2, 10);

    printf("vec1: ");
    print_vector(vec1, 10);
    printf(" => vec2: ");
    print_vector(vec2, count);
    printf("\n\n");
}