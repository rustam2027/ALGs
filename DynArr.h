#include <stdio.h>
#include <stdlib.h>
#include "DynArr.c"


void nullcheck(void* ptr);

void init_DynArr(DynArr* ptr);

void realloc_DynArr(DynArr* ptr, size_t new_cap);

void add_to_DynArr(DynArr* ptr, int num);

int get_from_DynArr(DynArr* ptr, size_t i);

int get_last_DynArr(DynArr* ptr);

void del_elem_DynArr(DynArr* ptr, size_t i);

void del_last_DynArr(DynArr* ptr);

void print_DynArr(DynArr* ptr);

void free_DynArr(DynArr* ptr);
