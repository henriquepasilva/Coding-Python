#include <stdio.h>

char toupper_custom(char c) {
    if (c >= 'a' && c <= 'z')
        return c - 'a' + 'A';
    return c;
}

int main () {
    char str[] = "Fundamentos da Programacao";
    for (int i = 0; str[i] != 0; i++) {
        str[i] = toupper_custom(str[i]); 
    }
    
    printf("String em maiusculas: %s\n\n", str);
}