class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Fore Way
        # 1. Sore the array
        # 2. Iterate through the array 
            # a. start and check element before it has diff 1
                 # if its true then increase sequnce by 1 
                 # if not update the sequence count and return last

        sort_nums = sorted(nums)

        if nums == []:
            return 0
        
        len_list = len(nums)
        seq_count = 1
        max_count = 1

        for n in range(1,len_list):
            # Skip duplicates as they don't break or extend the streak
            if sort_nums[n] == sort_nums[n-1]:
                continue
            if sort_nums[n] - sort_nums[n-1] == 1:
                seq_count +=1
            else:
                # Sequence broke, reset the counter
                seq_count = 1
            max_count = max(max_count,seq_count)
        return max_count
