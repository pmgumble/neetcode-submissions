class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for element in nums:
            if element not in hashset:
                hashset.add(element)
            else:
                return True
                   
        return False