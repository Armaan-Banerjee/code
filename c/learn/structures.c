#include<stdio.h>
#include<string.h>

struct Computers{
    char name[20];
    char CPU[20]
    char GPU[20]
    int RAM;
};

int main(){
    struct Computers Dell;
    struct Computers Lenovo;

    strcpy(Dell.name, "XPS 15");
    strcpy(Dell.CPU, "Intel");
    strcpu(Dell.GPU, "N3060");
    Dell.RAM = 8000;

    strcpy(Lenovo.name, "Yoga");
    strcpy(Lenovo.CPU, "AMD");
    strcpy(Lenovo.GPU, "Integrated");
    Lenovo.RAM = 4000;

    

}
