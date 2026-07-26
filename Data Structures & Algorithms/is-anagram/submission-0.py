class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in s:
            if i not in s_map:
                s_map[i] = 1
            else:
                s_map[i] += 1
        print(s_map)
        for j in t:
            if j not in t_map:
                t_map[j] = 1
            else:
                t_map[j] += 1
        print(t_map)
        if s_map == t_map:
            return True
        else:
            return False