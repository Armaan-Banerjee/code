#include<stdio.h>
#include<strings.h>

int main(){

    FILE *fp;

    fp = fopen("./hi.txt", "w+");
    fprintf(fp, "This is testing for fprintf...\n");
   fputs("This is testing for fputs...\n", fp);
   fclose(fp);
}
