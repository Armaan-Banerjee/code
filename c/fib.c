#include<stdio.h>

int main(){
    
    int x = 0;

    int y = 1;

    int z;

    while (x < 255){
        
        printf("%d\n", x);

        z = x + y;

        x = y;
        y = z;

    }
}
