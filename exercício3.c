#include <stdio.h>
#include <string.h>

typedef struct {
    int nota;
    char nome[11];
} disciplina_tipo;

typedef struct _aluno {
    char nome[20];
    char apelido[20];
    int idade;
    disciplina_tipo disciplina;  
} aluno_tipo;

void preencherStruct(aluno_tipo *aluno) {
    printf("Nome: ");
    scanf("%s", aluno->nome);

    printf("Apelido: ");
    scanf("%s", aluno->apelido);

    printf("Idade: ");
    scanf("%d", &aluno->idade);

    printf("Nome da disciplina: ");
    scanf("%s", aluno->disciplina.nome);

    printf("Nota: ");
    scanf("%d", &aluno->disciplina.nota);
}

aluno_tipo preencherStruct_2() {
    aluno_tipo aluno;

    printf("Nome: ");
    scanf("%s", aluno.nome);

    printf("Apelido: ");
    scanf("%s", aluno.apelido);

    printf("Idade: ");
    scanf("%d", &aluno.idade);

    printf("Nome da disciplina: ");
    scanf("%s", aluno.disciplina.nome);

    printf("Nota: ");
    scanf("%d", &aluno.disciplina.nota);

    return aluno;
}

void mostrarStruct(aluno_tipo aluno) {
    printf("\n--- Dados do Aluno ---\n");
    printf("Nome: %s %s\n", aluno.nome, aluno.apelido);
    printf("Idade: %d\n", aluno.idade);
    printf("Disciplina: %s\n", aluno.disciplina.nome);
    printf("Nota: %d\n", aluno.disciplina.nota);
}

int main() {
    aluno_tipo a1, a2;

    printf("=== Preenchimento com ponteiro ===\n");
    preencherStruct(&a1);
    mostrarStruct(a1);

    printf("\n=== Preenchimento com retorno ===\n");
    a2 = preencherStruct_2();
    mostrarStruct(a2);

    return 0;
}