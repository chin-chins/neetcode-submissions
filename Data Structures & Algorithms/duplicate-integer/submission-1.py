class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = dict()
        for x in nums:
            dups.update(nums)
            if dups.size() < nums.size():
                return true

        return false 
        
        