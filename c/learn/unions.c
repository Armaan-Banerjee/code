#include <stdio.h>
#include <string.h>
 
union Data {
   int i;
   float f;
   char str[20];
};
 
int main( ) {

    union Data data;        

    printf( "Memory size occupied by data : %ld\n", sizeof(data));
    

    data.i = 8;
    data.f = 90.9;
    data.str = "hi there";

    printf("i: %i\n", data.i);
    printf("f : %f\n", data.f);
    printf("str: %s\n", data.str);

    return 0;
}

