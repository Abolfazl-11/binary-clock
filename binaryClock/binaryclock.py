import datetime
import decimaltobinary

#clock style
#  --##-#
#  #-##--
#  13: 44

time = datetime.datetime.now()
h = time.hour
m = time.minute
lastm = m

for r in range(2):                       
     num = h if r == 0 else m                 
     b = decimaltobinary.dectobin(num, 6)                          
     for c in b:                        
         char = "#" if c == "1" else "-"      
         print(char, end="")          
     print("")                          
print(f"{h}: {m}")

while True:
    time = datetime.datetime.now()
    h = time.hour
    m = time.minute

    if lastm != m:
        print("\n******\n")
        for r in range(2):
            num = h if r == 0 else m
            b = decimaltobinary.dectobin(num, 6)
            for c in b:
                char = "#" if c == "1" else "-"
                print(char, end="")
            print("")
            lastm = m
        print(f"{h}: {m}")
