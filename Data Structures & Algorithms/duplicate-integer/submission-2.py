class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for x in nums:
            if x in dups:
                return True
            dups.add(x)

        return False