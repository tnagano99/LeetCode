class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mn = 0
        mx = len(nums) - 1
        mid = 0
        while mn <= mx:
            mid = mn + (mx - mn) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                mx = mid - 1
            elif nums[mid] < target:
                mn = mid + 1
        return mn