class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        count = 0
        val = n - 1
        n1 = 1
        n2 = 1
        tot = 0
        while count < val:
            tot = n1 + n2
            n1 = n2
            n2 = tot
            count += 1

        return tot


        