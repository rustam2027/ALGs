#include <stdlib.h>
#include <stdio.h>


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

    int i = l;
    int j = l + 1;

    int pivot = l + rand() % (r - l);

    swap(nums, l, pivot);

    while (j <= r){
        if (nums[j] < nums[l]){
            i++;
            swap(nums, i, j);
        }
        j++;
    }

    swap(nums, l, i);

    if (i > r){
        return 0;
    }

    sortArrayRecursion(nums, l, i);
    sortArrayRecursion(nums, i + 1, r);

    return 0;
}


int* sortArray(int* nums, int numsSize, int* returnSize){
    int* returnNums = (int*) malloc(numsSize * sizeof(int));

    sortArrayRecursion(nums, 0, numsSize - 1);

    for (int i = 0; i < numsSize; i++){
        returnNums[i] = nums[i];
    }

    *returnSize = numsSize;

    return returnNums;
}

int main(){
    int* A = (int*) malloc(8 * sizeof(int));

    for (int i = 0; i < 8; i ++){

    }

    int l;

    int* B = sortArray(A, 8, &l);

    for (int i = 0; i < l; i++){
        printf("%d ", B[i]);
    }

    printf("\n");
}
