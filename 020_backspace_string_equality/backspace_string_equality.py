def main():
    print(backspace_string_equality("abc####", "abf#"))

def backspace_string_equality(s, t):
    s = backspace_string(s)
    t = backspace_string(t)
    print(s + " " + t)
    return s == t

def backspace_string(in_strint):
    result = str()
    for ch in in_strint:
        if ch == "#":
            try:
                result = result[:-1]
            except IndexError:
                result = ""
        else:
            result += ch
    return result
    

if __name__ == "__main__":
    main()