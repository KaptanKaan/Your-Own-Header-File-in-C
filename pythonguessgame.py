from random import randrange
n=randrange(1000)
while True:
    k=int(input())
    if(k==n):
        print("YOU WİN")
        break
    print("BİGGER" if(k<n) else "SMALLER")
