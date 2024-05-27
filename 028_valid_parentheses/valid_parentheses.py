class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_pairs = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        
        open_braces = []
        for ch in s:
            if ch in bracket_pairs:
                open_braces.append(ch)
            elif bracket_pairs[open_braces.pop()] == ch:
                pass
            else:
                return False
        return True


def main():
    tester = Solution()
    print(tester.isValid(r"()[]{}"))

if __name__ == "__main__":
    main()