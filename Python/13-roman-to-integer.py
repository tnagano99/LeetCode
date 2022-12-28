class Solution:
    def romanToInt(self, s: str) -> int:
        ls = list(s)
        ls_ds = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}

        nums = [ls_ds[num] for num in ls]
        total = 0
        flag = False
        for i in range(len(nums)-1):
            if nums[i] >= nums[i + 1] and not flag:
                total += nums[i]
                flag = False
            elif not flag:
                total += nums[i + 1] - nums[i]
                flag = True
            else:
                flag = False
                continue
        
        if not flag:
            total += nums[-1]

        return total