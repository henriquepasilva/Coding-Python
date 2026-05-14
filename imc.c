#include <stdio.h>

int main() {
    float peso, altura, imc;
    
    printf("O seu peso é: ");
    scanf("%f", &peso);
    
    printf("A sua altura é: ");
    scanf("%f", &altura);

    imc = peso/(altura * altura);
    printf("O seu IMC é: %.2f\n", imc);

    if (imc <= 19){
        printf("Você está abaixo do peso normal!");
    }
    else if (19 < imc && imc <=25){
        printf("Você está no peso normal!");
    }
    else if (25 < imc && imc <= 30){
        printf("Você está acima do peso!");
    }
    else if (30 < imc){
        printf("Você está obeso!Pare de comer por amor de deus!");
    }
   

    return 0;
}