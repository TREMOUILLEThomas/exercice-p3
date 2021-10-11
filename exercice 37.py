n=int(input("choisir un nombre : "))
for i in range(n):
    b=n%(i+1)
    if b==0:
        print (i+1)