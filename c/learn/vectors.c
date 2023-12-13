#include <stdio.h>
#include <math.h>

float dot_product(float vector_a[], float vector_b[], size_t size_a, size_t size_b) {
    float total = 0;

    if (size_a != size_b) {
        return -1;
    }

    for (int i = 0; i < size_a; i++ ){
        float dot = vector_a[i] * vector_b[i];
        total += dot;
    }

    return total;

}

float *cross_product(float vector_a[], float vector_b[]){
    static float cross_vec[3];

    cross_vec[0] = (vector_a[1] * vector_b[2]) - (vector_a[2] * vector_b[1]);
    cross_vec[1] = (vector_a[2] * vector_b[0]) - (vector_a[0] * vector_b[2]);
    cross_vec[2] = (vector_a[0] * vector_b[1]) - (vector_a[1] * vector_b[0]);

    return cross_vec; 

}

float *add_vecs(float vector_a[], float vector_b[], size_t size_a, size_t size_b){

    size_t size;
    
    if (size_a > size_b) {
        size = size_a;
    } else {
        size = size_b;
    }

    float added_vec[size];

    for (int i = 0; i < size; i++){
        added_vec[i] = vector_a[i] + vector_b[i];
    }

    return added_vec;


}

float magnitude(float vector[], size_t size_vec){

    double mag_sq = 0;
    
    for (int i = 0; i < size_vec; i++){
        mag_sq += vector[i] * vector[i];
    }

    return sqrt(mag_sq);

}


int main(){

    float vec_a[3] = {1, 2, 3};

    float vec_b[3] = {1, 4, 3};

    size_t size_vec_a = sizeof(vec_a) / sizeof(vec_a[0]);
    size_t size_vec_b = sizeof(vec_b) / sizeof(vec_b[0]);

    //for (int i = 0; i < size_vec_a; i++){
        //printf("%s : %f  %s : %f ", "a", vec_a[i], "b", vec_b[i]);
        //printf("\n");
    //}

    float result_dot = dot_product(vec_a, vec_b, size_vec_a, size_vec_b);

    printf("%s %f %s", "dot_product:", result_dot, "\n");

    float *result_cross;

    result_cross = cross_product(vec_a, vec_b);


    printf("%s", "cross product: \n");

    for (int i = 0; i < 3; i++) {
        char* out;
        if (i == 0) {
            out = "i";
        } 
        else if (i == 1){
            out = "j";
        }
        else if (i == 2){
            out = "k";
        }

        printf("%s : %f %s" , out , result_cross[i], "\n");

    }

    float *added_result;

    added_result = add_vecs(vec_a, vec_b, size_vec_a, size_vec_b);

    printf("\n added vectors \n");

    for (int i = 0; i < size_vec_a; i++){
        printf("%f", added_result[i]);
    }

    printf("\n magnitude vector a: \n");
    double mag_a = magnitude(vec_a, size_vec_a);
    printf("%f", mag_a);

    printf("\n magnitude vector b: \n");
    double mag_b = magnitude(vec_b, size_vec_b);
    printf("%f", mag_b);

}