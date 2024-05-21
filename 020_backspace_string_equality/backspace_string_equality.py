def main():
    s = "a###b#c#d"
    t = "d"
    print(Solution.backspace_string_equality(s, t))
    print(backspace_string_equality_bf(s,t))

class Solution():
    @classmethod
    def backspace_string_equality(cls,s,t):
        s_i, t_i = -1, -1
        while True:
            
            if s_i >= -len(s):
                if s[s_i] == "#":
                        s_i = cls.process_backspaces(s, s_i)
            if t_i >= -len(t):
                if t[t_i] == "#":
                        t_i = cls.process_backspaces(t, t_i)

            if t_i >= -len(t) and s_i >= -len(s):
                if s[s_i] == t[t_i]:
                    s_i -= 1
                    t_i -= 1 

                elif s[s_i] != t[t_i]:
                    return False

            else:
                if s_i + len(s) < 0 and t_i + len(t) < 0:
                    return True
                else:
                    return False
    
    @classmethod
    def process_backspaces(cls, data, index):
        skip_factor = 0
        while True:
            if index < -len(data):
                return index
            if data[index] == '#':
                skip_factor += 2
            elif skip_factor > 0:
                skip_factor -= 1
            else:
                return index
            index -= 1




def backspace_string_equality_bf(s, t):
    return backspace_string(s) == backspace_string(t)

def backspace_string(in_strint):
    result = []
    for ch in in_strint:
        if ch == "#":
            try:
                result.pop()
            except IndexError:
                pass
        else:
            result.append(ch)
    return result
    

if __name__ == "__main__":
    main()


def backspace_string_equality_bf(s, t):
    s = backspace_string(s)
    t = backspace_string(t)
    return s == t

def backspace_string(in_strint):
    result = []
    for ch in in_strint:
        if ch == "#":
            try:
                result.pop()
            except IndexError:
                pass
        else:
            result.append(ch)
    return result
    

if __name__ == "__main__":
    main()