#include <stdlib.h>
#include <stdio.h>
#include <time.h>


void print_arr(int* arr, int len){
    for (int i = 0; i < len; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void swap(int* first, int* last){
    int buffer = *first;
    *first = *last;
    *last = buffer;
}


int sortArrayRecursion(int* first, int* last){
    if (last - first < 2){
        return 0;
    }

    if (*first > *last){
        swap(first, last);
    }

    int* pivot_pos = first;
    int pivot = *first;

    do {
        first++;
    } while(*first < pivot);

    for (int* i = first + 1; i < last; i++){
        int x = *i;
        int smaller = - (int) (x < pivot);
        int delta = smaller & (i - first);
        first[delta] = *first;
        i[-delta] = x;
        first -= smaller;
    }
    first --;
    *pivot_pos = *first;
    *first = pivot;

    sortArrayRecursion(first, pivot_pos);
    sortArrayRecursion(pivot_pos + 1, last);

    return 0;
}


void sortArray(int* nums, int numsSize){
    sortArrayRecursion(nums, nums + numsSize);
}


int get_data(int* nums, FILE* file){
    char c = fgetc(file);
    int i = 0;
    int num = 0;
    int sign = 1;

    while (c != EOF){
        if (c == ' ' || c == '\n'){
            nums[i++] = num * sign;
            num = 0;
            sign = 1;
        } else if (c == '-'){
            sign = -1;
        } else {
            num = num * 10;
            num += c - '0';
        }
        c = fgetc(file);
    }

    return i - 1;
}


int main(int argc, char * argv[]){
    FILE* input = fopen(argv[1], "r");

    int* nums = (int*) malloc(sizeof(int) * 1000000);

    int len = get_data(nums, input);

    fclose(input);

    clock_t start = clock();

    sortArray(nums, len);

    clock_t end = clock();

    double spent_time = (double) (end - start) / CLOCKS_PER_SEC;

    FILE* output = fopen("out.txt", "w");

    fprintf(output, "%f \n", spent_time);

    fclose(output);
    free(nums);
}