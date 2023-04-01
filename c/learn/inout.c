#include <stdio.h>

int main() {

    char str[100];

    printf( "Enter a value :");
    gets(str);

    printf( "\nYou entered: ");
    puts(str);
    
    char astr[100];

    int i; 

    printf("Enter a nother value");
    scanf("%s %d", str, &i);

   return 0;
}
