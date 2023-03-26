#include <stdlib.h>
#include <stdio.h>
#include <time.h>


void print_arr(int* arr, int len){
    for (int i = 0; i < len; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}


void swap(int* nums, int l, int r){
    int buffer;

    buffer = nums[l];
    nums[l] = nums[r];
    nums[r] = buffer;
}


int sortArrayRecursion(int* nums, int l, int r){
    if (r - l <= 0){
        return 0;
    } else if (r - l == 1){
        if (nums[l] > nums[r]){
            swap(nums, l, r);
        }
        return 0;
    }

    if (nums[l] > nums[r]){
        swap(nums, l, r);
    }

    int pivot_pos = l;
    int pivot = nums[l];

    do {
        l++;
    } while(nums[l] < pivot);

    for (int i = l + 1; i < r; i++){
        int x = nums[i];
        int smaller = - (int) (x < pivot);
        int delta = smaller & (i - l);
        nums[l + delta] = nums[l];
        nums[i - delta] = x;
        l -= smaller;
    }
    l --;
    nums[pivot_pos] = nums[l];
    nums[l] = pivot;

    sortArrayRecursion(nums, l, pivot_pos);
    sortArrayRecursion(nums, pivot_pos + 1, r);

    return 0;
}


void sortArray(int* nums, int numsSize){
    int* returnNums = (int*) malloc(numsSize * sizeof(int));

    sortArrayRecursion(nums, 0, numsSize - 1);

    for (int i = 0; i < numsSize; i++){
        returnNums[i] = nums[i];
    }
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

    int* nums = (int*) malloc(sizeof(int) * 10000);

    int len = get_data(nums, input);

    fclose(input);

    clock_t start = clock();

    sortArray(nums, len + 1);

    clock_t end = clock();

    double spent_time = (double) (end - start) / CLOCKS_PER_SEC;

    FILE* output = fopen("out.txt", "w");

    fprintf(output, "%f \n", spent_time);

    fclose(output);
    free(nums);
}