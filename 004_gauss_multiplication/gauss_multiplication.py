import math

def gauss_multiplication(x, y):
    
    
    len_xy = max(len(str(x)), len(str(y)))
    len_xy_min = min(len(str(x)), len(str(y)))
    
    if len(str(x)) <=1 or len(str(y)) <= 1:
        return x*y
    
    x, y = str(x), str(y)
    
    x0, x1 = x[0:math.ceil(len(x)/2)], x[math.ceil(len(x)/2):]
    y0, y1 = y[0:math.ceil(len(y)/2)], y[math.ceil(len(y)/2):]

    x1, x0, y1, y0 = int(x0), int(x1), int(y0), int(y1)

    if len_xy>2:
        u = gauss_multiplication(x1, y1)
        v = gauss_multiplication(x0, y0)
        w = gauss_multiplication(x1+x0, y1+y0)
    else:
        u = x1*y1
        v = x0*y0
        w = (x1 + x0)*(y1 + y0)

    z = w -u -v
    p1 =  u*(10**len_xy_min)
    p2 = z*(10**(len_xy_min//2))
    p = +  p1 + p2 + v

    return p


def main():
    a = 23
    b = 345

    p = gauss_multiplication(a,b) #7 006 652
    print(p)

if __name__ == "__main__":
    main()