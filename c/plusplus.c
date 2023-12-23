#include<stdio.h>

int main(){
    
    int num = 0;

    for (int i = 0; i < 10000000; i++){
        num += 1;
    }

    printf("%d", num);

}
