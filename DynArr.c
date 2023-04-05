#include <stdlib.h>
#include <stdio.h>


void nullcheck(void* ptr){
    if (ptr == NULL){
        fprintf(stderr, "ERROR: OUT OF MEMORY!\n");
        exit(1);
    }
}


typedef struct{
    size_t len;
    size_t cap;
    int* value;
} DynArr;


void init_DynArr(DynArr* ptr){
    ptr->cap = 1;
    ptr->len = 0;
    ptr->value = (int*) malloc(sizeof(int) * ptr->cap);
    nullcheck(ptr->value);
}


void realloc_DynArr(DynArr* ptr, size_t new_cap){
    ptr->cap = new_cap;
    ptr->value = (int*) realloc(ptr->value, ptr->cap);
    nullcheck(ptr->value);
}


void add_to_DynArr(DynArr* ptr, int num){
    if(ptr->cap < ptr->len + 1){
        realloc_DynArr(ptr, ptr->cap * 2);
    }
    ptr->value[ptr->len++] = num;
}


int get_from_DynArr(DynArr* ptr, size_t i){
    if (i >= ptr->len){
        fprintf(stderr, "ERROR: INDEX OUT OF RANGE (%lu >= %lu)\n", i, ptr->len);
        exit(2);
    }
    return ptr->value[i];
}

void del_elem_DynArr(DynArr* ptr, size_t i){
    if (i >= ptr->len){
        fprintf(stderr, "ERROR: DELETING ELEMENT THAT DOESNT EXIST\n");
        exit(3);
    }
    if (i + 1 != ptr->len){
        for(size_t j = i; j < ptr->len - 1; j++){
            ptr->value[j] = ptr->value[j + 1];
        }
    }
    ptr->len -= 1;
    if  (ptr->len <= (ptr->cap / 4)){
        realloc_DynArr(ptr, ptr->cap / 2);
    }
}


void print_DynArr(DynArr* ptr){
    printf("[");
    size_t i = 0;
    for (; i + 1 < ptr->len; i++){
        printf("%d", ptr->value[i]);
        printf(", ");
    }
    printf("%d]\n", ptr->value[i]);
}


void free_DynArr(DynArr* ptr){
    free(ptr->value);
    ptr->cap = 0;
    ptr->len = 0;
}


int main(){
    DynArr A;
    init_DynArr(&A);
    add_to_DynArr(&A, 6);
    add_to_DynArr(&A, 7);
    add_to_DynArr(&A, 9);
    add_to_DynArr(&A, 10);
    add_to_DynArr(&A, 11);
    printf("%d\n", get_from_DynArr(&A, 1));
    print_DynArr(&A);
    free_DynArr(&A);
}
