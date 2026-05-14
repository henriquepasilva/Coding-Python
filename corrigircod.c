#include<stdio.h>

int main() {
    int idade;
    printf(" Digite qual a sua idade: ");
    scanf ("%d",&idade);

    if (idade<21)
        printf("A sua idade é inferior a 21 anos! \n\n");
    else if(idade>21)
        printf ("A sua idade é superior a 21 anos! \n\n");
    else printf ("A sua idade é igual a 21 anos! \n\n");

    return 0;


}