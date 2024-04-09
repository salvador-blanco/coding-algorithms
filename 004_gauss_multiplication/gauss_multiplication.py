def gauss_multiplication(x, y):
    
    x, y = str(x), str(y)
    len_xy = len(x)
    x0, x1 = x[0:len_xy//2], x[len_xy//2:]
    y0, y1 = y[0:len_xy//2], y[len_xy//2:]

    x1, x0, y1, y0 = int(x0), int(x1), int(y0), int(y1)

    if len_xy>2:
        u = gauss_multiplication(x1, y1)
        v = gauss_multiplication(x0, y0)
        w = gauss_multiplication(x1+x0, y1+y0)
    else:
        u = x1*y1
        v = x0*y0
        w = (x1 + x0)*(y1 + y0)

    z = w - (u+v)
    p = u*(10**len_xy) + z*(10**(len_xy//2)) + v

    return p

def main():
    a = 1234
    b = 5678
    p = gauss_multiplication(a,b) #7 006 652
    print(p)
if __name__ == "__main__":
    main()