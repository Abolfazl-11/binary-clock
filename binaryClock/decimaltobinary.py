def dectobin(n:int, d:int):
    num = n
    b = [0 for i in range(d)]
    for i in range(d, 0, -1):
        a = num // (2**(i - 1))                          
        b[d - i] = str(a)                            
        num -= (2**(i - 1)) * a                          
    return ''.join(b)

if __name__ == "__main__":
    num, digit = [int(i) for i in input().split()]
    r = dectobin(num, digit)
    print(r)