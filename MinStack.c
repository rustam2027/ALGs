#include "Stack.h"


typedef struct {
    Stack* main;
    Stack* min;
} MinStack;


MinStack* minStackCreate() {
    MinStack* min_stack = (MinStack*) malloc(sizeof(MinStack));
    min_stack->main = init_stack();
    min_stack->min = init_stack();
    return min_stack;
}

void minStackPush(MinStack* obj, int val) {
    int pre_min = INT32_MAX;
    if (obj->min->array->len > 0){
        pre_min = check_stack(obj->min);
    }
    if (val <= pre_min){
        push_stack(obj->min, val);
    }
    push_stack(obj->main, val);
}

void minStackPop(MinStack* obj) {
    int min = check_stack(obj->min);
    if (min == pop_stack(obj->main)){
        pop_stack(obj->min);
    }
}

int minStackTop(MinStack* obj) {
    return check_stack(obj->main);
}

int minStackGetMin(MinStack* obj) {
    return check_stack(obj->min);
}

void minStackFree(MinStack* obj) {
    free_stack(obj->main);
    free_stack(obj->min);
    free(obj);
}


int main(){
    MinStack* A = minStackCreate();
    minStackPush(A, 0);
    minStackPush(A, 1);
    minStackPush(A, 0);
    printf("%d\n", minStackGetMin(A));
    minStackPop(A);
    printf("%d\n", minStackGetMin(A));
    minStackFree(A);
}
