#include <stdio.h>
#include <stdlib.h>
#include "Stack.c"


Stack* init_stack();

void push_stack(Stack* ptr, int num);

int pop_stack(Stack* ptr);

int check_stack(Stack* ptr);

void free_stack(Stack* ptr);

void print_stack(Stack* ptr);
