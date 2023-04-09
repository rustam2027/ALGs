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
    ptr->value = (int*) realloc(ptr->value, sizeof(int) * ptr->cap);
    nullcheck(ptr->value);
}


void add_to_DynArr(DynArr* ptr, int num){
    if(ptr->cap < ptr->len + 1){
        realloc_DynArr(ptr, ptr->cap * 2);
    }
    ptr->value[ptr->len] = num;
    ptr->len++;
}


int get_from_DynArr(DynArr* ptr, size_t i){
    if (i >= ptr->len){
        fprintf(stderr, "ERROR: INDEX OUT OF RANGE\n");
        exit(2);
    }
    return ptr->value[i];
}


int get_last_DynArr(DynArr* ptr){
    if (ptr->len == 0){
        fprintf(stderr, "ERROR: INDEX OUT OF RANGE\n");
        exit(2);
    }
    return get_from_DynArr(ptr, ptr->len - 1);
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
    if  (ptr->len + 1 <= (ptr->cap / 4)){
        realloc_DynArr(ptr, ptr->cap / 2);
    }
}


void del_last_DynArr(DynArr* ptr){
    if (ptr->len == 0){
        fprintf(stderr, "ERROR: DELETING ELEMENT THAT DOESNT EXIST\n");
        exit(3);
    }
    del_elem_DynArr(ptr, ptr->len - 1);
}


void print_DynArr(DynArr* ptr){
    printf("[");
    size_t i = 0;
    for (; i + 1 < ptr->len; i++){
        printf("%d", ptr->value[i]);
        printf(", ");
    }
    if (ptr->len > 0){
        printf("%d]\n", ptr->value[i]);
    } else {
        printf("]\n");
    }
}


void free_DynArr(DynArr* ptr){
    free(ptr->value);
    ptr->cap = 0;
    ptr->len = 0;
}
