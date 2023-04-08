#include <stdio.h>
#include <stdlib.h>
#include "DynArr.h"


typedef struct {
    DynArr* array;
} Stack;


Stack* init_stack(){
    Stack* return_stack = (Stack*) malloc(sizeof(Stack));
    DynArr* arr = (DynArr*) malloc(sizeof(DynArr));
    init_DynArr(arr);
    return_stack->array = arr;
    return return_stack;
}

void push_stack(Stack* ptr, int num){
    add_to_DynArr(ptr->array, num);
}

int pop_stack(Stack* ptr){
    int return_int = get_last_DynArr(ptr->array);
    del_last_DynArr(ptr->array);
    return return_int;
}

int check_stack(Stack* ptr){
    int return_int = get_last_DynArr(ptr->array);
    return return_int;
}

void free_stack(Stack* ptr){
    free_DynArr(ptr->array);
    free(ptr);
}
