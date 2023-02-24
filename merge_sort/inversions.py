local_inversions = 0
global_inversions = 0


class Solution:
    def isIdealPermutation(self, nums) -> bool:
        if len(nums) == 1:
            return True
        
        global local_inversions
        global global_inversions
        
        local_inversions = 0
        global_inversions = 0
        

        def merging(left_edge_1, right_edge_1, left_edge_2, right_edge_2, result, array, buffer):
            global local_inversions
            global global_inversions

            i = 0
            len_array = right_edge_1 - left_edge_1 + right_edge_2 - left_edge_2 + 2
            while left_edge_1 <= right_edge_1 and left_edge_2 <= right_edge_2:
                if array[left_edge_1] <= array[left_edge_2]:
                    buffer[i] = array[left_edge_1]
                    left_edge_1 += 1
                else:
                    global_inversions += right_edge_1 - left_edge_1 + 1
                    buffer[i] = array[left_edge_2]
                    left_edge_2 += 1
                i += 1

            while left_edge_1 <= right_edge_1:
                buffer[i] = array[left_edge_1]
                i += 1
                left_edge_1 += 1

            while left_edge_2 <= right_edge_2:
                buffer[i] = array[left_edge_2]
                i += 1
                left_edge_2 += 1
            
            
            for i in range(len_array):
                array[result + i] = buffer[i]
                

        def merge_sort(left_index, right_index, array):
            global local_inversions
            global global_inversions

            if right_index - left_index == 0:
                return 0
            elif right_index - left_index == 1:
                if array[right_index] < array[left_index]:
                    array[right_index], array[left_index] = array[left_index], array[right_index]
                    global_inversions += 1
                    local_inversions += 1
                return 0
            
            pivot = (right_index + left_index) // 2
            
            if array[pivot] > array[pivot + 1]:
                local_inversions += 1
            
            merge_sort(left_index, pivot, array)
            merge_sort(pivot + 1, right_index, array)
            
            buff = [0] * len(array)
            merging(left_index, pivot, pivot + 1, right_index, left_index, array, buff)
        
        merge_sort(0, len(nums) - 1, nums)

        return global_inversions == local_inversions
