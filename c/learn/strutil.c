#include<stdio.h>
#include<strings.h>

int main() {
    char string1[20] = "hi there";
    char string2[20];

    strcpy(string2, string1);
    puts(string2);
    puts(string1);


}
