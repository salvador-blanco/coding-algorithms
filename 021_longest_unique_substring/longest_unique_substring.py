def main():
    tester = Solution()
    input_s = "pwwkew"
    print(tester.lengthOfLongestSubstring(input_s))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            max_len = 0
            l, r, = 0, 0

            while r < len(s):
                if s[r] in s[l:r]:
                    l += 1
                else:
                    r += 1
                    if r-l > max_len:
                        max_len = r-l
                     
            return max_len
                          
    
if __name__ == "__main__":
    main()