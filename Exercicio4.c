#include <stdio.h>

typedef struct {
    char nome[61];
    char curso[21];
    char estatuto;
    int num_disciplinas;
    int notas[30];

} Estudante;

float aluno_media(Estudante e) {
    int soma = 0;
    for ( int i = 0; i < e.num_disciplinas; i++) {
        soma += e.notas[i];
    }
    return (float)soma / e.num_disciplinas;
}

void exportar_dados(Estudante turma[], int n) {
    FILE *f = fopen("registos.txt", "w");
    if (!f) {
        printf("Erro ao abrir ficheiro.\n");
        return;
    }

    for (int i = 0; i < n; i++){
        fprintf(f, "%s %s %c [", turma[i].nome, turma[i].curso, turma[i].estatuto);
        for (int j = 0; j < turma[i].num_disciplinas; j++) {
            fprintf(f, "%d", turma[i].notas[j]);
            if (j < turma[i].num_disciplinas - 1) fprintf(f, " ");
        }
        fprintf(f , "]\n");
    }
    fclose(f);
}

int main() {
    Estudante turma[3] = {
        {"Henrique Silva", "Eng. Informatica", 't', 4, {10, 12, 13, 17}},
        {"Ana Costa", "Matematica", 'o', 3, {14, 15, 16}},
        {"Rui Dias", "Biologia", 'd', 2, {13, 15}}
    };

    for (int i = 0; i < 3; i++) {
        printf("Média do aluno %s: %.2f\n", turma[i].nome, aluno_media(turma[i]));
    }

    exportar_dados(turma, 3);
    printf("\nDados exportados para 'Registos.txt' \n\n");
}
