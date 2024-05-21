from collections import dque

def main():
    tester = Solution(input_s)
    input_s = "pwwkew"
    print(tester.lengthOfLongestSubstring(input_s))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            stack = dque()
            max_len = len(stack)
            i = 0
            len_text = len(s)

            while i < len_text:
                if not s[i] in stack:
                     stack.append(s[i])
                     max_len = max(max_len, len(stack))
                else:
                     stack.popleft()
            return max_len
                          
    
if __name__ == "__main__":
    main()