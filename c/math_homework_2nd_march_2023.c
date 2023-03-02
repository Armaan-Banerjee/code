#include <stdio.h>

int seq(int num){
    int square = num * num;
    int variable_remover = 8 * num;
    return square - variable_remover - 5;
}

int main(){
    while (1) {
        int i = 1;
        int ans = seq(i);
        if( ans > 0 ) {
            printf("%d", , ii );
            break;
        }
        else {
            i++;
        }
    }
}
