import math

def gauss_multiplication(x, y):
    

    x, y = str(x), str(y)
    
    len_x = len(x)
    len_y = len(y)
    
    if len_x <=1 or len_y <= 1:
        return int(x)*int(y)

    len_xy = min(len_x, len_y)
    m = math.ceil(len_xy/2)
    
    x1, x0 = x[0:-m], x[-m:]
    y1, y0 = y[0:-m], y[-m:]

    x0, x1, y0, y1 = int(x0), int(x1), int(y0), int(y1)

    if len_xy>2:
        z2 = gauss_multiplication(x1, y1)
        z0 = gauss_multiplication(x0, y0)
        z1 = gauss_multiplication(x1+x0, y1+y0) - z2 - z0
    else:
        z2 = x1*y1
        z0 = x0*y0
        z1 = (x1 + x0)*(y0 + y1) - z2 -z0
        
    p1 = int(str(z2) + "0"*2*m ) #z2*(10**m)**2
    p2 = int(str(z1) + "0"*1*m ) #z1*(10**m)**1
    p3 = z0 #z0*(10**m)**0
    p = p1 + p2 + p3

    return p

def main():
    import time

    a = 234324
    b = 567556
    
    p = gauss_multiplication(a,b)
    
    print(f"Expected resutl: {a*b}")
    print(f"Karatsuba mult esult: {p}")
if __name__ == "__main__":
    main()