class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tot = bin(int(a,2) + int(b,2))
        return tot[2:]