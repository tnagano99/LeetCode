class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for i in range(len(digits) - 1, -1, -1):
            total += digits[i] * 10 ** (len(digits) - i - 1)
        
        total += 1
        str_total = str(total)
        digits = [int(str_total[i]) for i in range(len(str_total))]

        return digits