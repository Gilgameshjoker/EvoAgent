from collections import Counter, defaultdict

s = "ADOBECODEBANC"
t = "ABC"

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 记录窗口串跟子串

        cnt_s = Counter()
        cnt_t = Counter(t)
        ans_left,ans_right=-1,len(s)
        left = 0
        for right,c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:
                if right - left < ans_right - ans_left:
                    ans_left,ans_right = left,right
                cnt_s[s[left]] -= 1
                left += 1
        return "" if ans_left == -1 else s[ans_left:ans_right+1]

        """
        diff = defaultdict(int)
        for c in t:
            diff[c] -= 1
            print(diff)
        kinds = len(diff)
        print(kinds)

        ans_left,ans_right = -1,len(s)
        ge_cnt = 0
        left = 0

        for right,c in enumerate(s):
            diff[c] += 1
            print(diff)
            if diff[c] == 0:
                ge_cnt += 1
        """



solution = Solution()
print(solution.minWindow(s,t))