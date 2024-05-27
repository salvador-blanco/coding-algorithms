
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        open_braces = []
        close_braces = []
        for i, ch in enumerate(s):
            
            if ch == "(":
                open_braces.append(i)
            elif ch == ")":
                close_braces.append(i)

        while open_braces or close_braces:
             
            if not open_braces and close_braces:
                c = close_braces.pop()
                s=s[:c]+" "+s[c+1:]
            elif  open_braces and not close_braces:
                o = open_braces.pop()
                s=s[:o]+" "+s[o+1:]
            elif open_braces[-1] > close_braces[-1]:
                o = open_braces.pop()
                s=s[:o]+" "+s[o+1:]
            elif open_braces[-1] < close_braces[-1]:
                open_braces.pop()
                close_braces.pop()
        return s.replace(" ", "")

            

def main():
    tester = Solution()
    test_case_1 = "lee(t(c)o)de)"
    test_case_2 = "a)b(c)d"
    test_case_3 = "))(("
    test_case_4 = "())()((("
    test_case_5 = "(a(b(c)d)"

    print(tester.minRemoveToMakeValid(test_case_1))
    print()
    
    print(tester.minRemoveToMakeValid(test_case_2))
    print()

    print(tester.minRemoveToMakeValid(test_case_3))
    print()

    print(tester.minRemoveToMakeValid(test_case_4))
    print()

    print(tester.minRemoveToMakeValid(test_case_5))
    


if __name__ == "__main__":
    main()