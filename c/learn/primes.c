#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

bool is_prime(int num){

    bool has_factor = false;
    for (int i = 2; i < sqrt(num); i++){
        if (num % i == 0){
            has_factor = true;
            break;
        }
    }

    if (has_factor == false){
        return true;
    } else {
        return false;
    }
}

int *primes(int lb, int ub){

    int data_count = 0;

    for (int i = lb; i <= ub; i++){
        bool res = is_prime(i);

        if (res == true) {
            data_count += 1;
        }
    }

    int* results = (int*)malloc(sizeof(int) * data_count);

    int index = 0;
    for (int j = lb; j <= ub; j++){
        if (is_prime(j) == true){
            results[index] = j;
            index += 1;
        }
    }

    return results;

}

int main(){
    int *prime = primes(1, 100);

    printf("Array of prime numbers: ");
    for (int i = 0; i < (sizeof(prime)/ prime[0]); i++) {
        printf("%d ", prime[i]);
    }

    free(prime);
}