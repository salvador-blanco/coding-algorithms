import re

def main():
    tester = Solution()
    input_s = "A0asdfa/*-*/s456554654654df"
    print(tester.isPalindrome(input_s))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-z0-9]","", s.lower())
        l, r = 0, len(s)-1

        while r> l:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
if __name__ == "__main__":
    main() 