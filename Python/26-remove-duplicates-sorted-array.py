class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if val < nums[i]:
                val = nums[i]
                nums[count] = nums[i]
                count += 1
            else:
                continue
        return count