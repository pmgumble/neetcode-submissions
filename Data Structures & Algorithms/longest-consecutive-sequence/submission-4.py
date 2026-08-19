class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Optimize solution
        # 1. Check the ele in list and its left ele 
          # if it is 1 less then we can start from that no.
        # 2. make a set of list 
        # 3. if 1 less than current element is not in set then we can start
        # add 1 in current element and if its in set inciment the counter by 1
        # if not update the counter and go till last and update counter and at last select max value
        num_set = set(nums)
        max_count = 0

        for n in nums:
            if (n-1) not in num_set:
                count = 1
                current_num = n

                # 2. Add 1 to current element and check if it's in the set
                while(current_num + 1) in num_set:
                    current_num += 1
                    count += 1

                # 3. Update the maximum count found so far
                max_count = max(max_count, count)
        return max_count