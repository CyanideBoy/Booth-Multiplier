def to_int(bin):
    x = int(bin, 2)

    if bin[0] == '1': 
       x -= 2**len(bin)
    
    return x


f = open("TRACEFILE.txt","w")
g = open("debug.txt","w")
for x in range(256):
    for y in range(256):
        
        s1 = bin(x)[2:].zfill(8)
        s2 = bin(y)[2:].zfill(8)

        sd1 = to_int(s1)
        sd2 = to_int(s2)

        sol = sd1*sd2
        
        ansb = bin(sol % (1<<16))[2:]
        g.write(s1+" "+str(sd1)+" "+s2+" "+str(sd2)+" "+str(sol)+" "+ansb.zfill(16)+" "+ansb+"\n")
        f.write(s1.zfill(8)+s2.zfill(8)+" "+ansb.zfill(16)+" 1111111111111111"+"\n")