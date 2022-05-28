def dectobin(n, d):
     num = n
     b = [0 for i in range(d)]  
     t = [1024, 512, 256, 128, 64 ,32, 16, 8, 4, 2, 1]
     t = t[len(t) - d:]
     for i in range(d):
         v = num // t[i]                          
         b[i] = str(v)                            
         num -= t[i] * v                          
     return "".join(b)

if __name__ == "__main__":
    num, digit = [int(i) for i in input().split()]
    print(binary(num, digit))
