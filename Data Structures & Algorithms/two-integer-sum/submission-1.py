class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # in hash_map we will store the key as value(no. from list)
        # and value as its indices
        hash_map = {}

        for i in range(len(nums)):
            number = target - nums[i]
            if number not in hash_map:
                hash_map[nums[i]] = i
            else:
                return  [hash_map[number],i]
