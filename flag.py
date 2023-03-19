class Solution:
    def sortColors(self, nums) -> None:
        i = -1
        j = len(nums)

        k = 0

        while k < len(nums) and i < j and k < j:
            if nums[k] == 2:
                j -= 1
                nums[k], nums[j] = nums[j], nums[k]

            if nums[k] == 0:
                i += 1
                nums[k], nums[i] = nums[i], nums[k]

            if nums[k] == 1 or k <= i:
                k += 1

            print(nums)
            print(k)
            print()

# https://leetcode.com/submissions/detail/916110351/
