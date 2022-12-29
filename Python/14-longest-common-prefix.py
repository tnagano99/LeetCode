class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for j in range(1, len(strs[0]) + 1):
            test = strs[0][:j]
            for i in range(1, len(strs)):
                if test == strs[i][:j]:
                    continue
                else:
                    return pre
            pre = test
        return pre

            