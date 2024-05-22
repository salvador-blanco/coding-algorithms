import re

def main():
    tester = Solution()
    input_s = "abca"
    
    print(tester.valid_palindrome(input_s))

class Solution:
    def valid_palindrome(self, s: str) -> bool:
        s = list(s)
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return self.mistmach_skip(s, left+1, right) or self.mistmach_skip(s, left, right-1) 
            left  += 1
            right -= 1    
        return True
        
    def mistmach_skip(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
if __name__ == "__main__":
    main() 