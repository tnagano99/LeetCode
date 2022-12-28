class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert to string
        xs = str(x)
        # account for odd or even lengths
        n = len(xs)
        if n % 2 == 0:
            fs = xs[:n//2]
            bs = xs[:n//2 - 1:-1]
            if fs == bs:
                return True
            else:
                return False
        else:
            fs = xs[:n//2]
            bs = xs[:n//2:-1]
            if fs == bs:
                return True
            else:
                return False