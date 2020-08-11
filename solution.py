def christmas_tree():
    s=chr(47)
    c=chr(92)
    d=chr(95)
    l=d+c
    r=s+d
    b=2
    i=13
    p=' '
    print(12*p+c+p+s)
    print(10*p+"-->*<--")
    print(12*p+s+d+c)
    while b<=6:
        print((i-b)*p+s+l*b)
        print((i-b-1)*p+r*(b+1)+c)
        b+=1
    print(11*p+"[___]")

if __name__ == "__main__":
    christmas_tree()