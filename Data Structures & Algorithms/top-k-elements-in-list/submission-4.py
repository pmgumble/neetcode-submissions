class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {} # store freq of occurence e.g 1:1, 2:2, 3:3
        # 1. Count the frequencies of each number
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1
            else:
                 hash_map[n] += 1
        print(hash_map)

        arr = []
        for key, val in hash_map.items():
            arr.append([val, key])
        print(arr)
        arr.sort()
        final_ans = []
        while len(final_ans) < k:
            final_ans.append(arr.pop()[1])
        return final_ans