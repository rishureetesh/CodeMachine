def NToOne(num):
    if num==0:
        return
    print(num)
    NToOne(num-1)

def OneToN(num):
    if num == 0:
        return
    OneToN(num-1)
    print(num)

NToOne(10)
OneToN(10)