n=int(input("choisir un nombre : "))
print("les diviseurs sont : ")
d=0
for i in range(1,n+1):
    b=n%(i)
    if b==0:
        d=d+1
        print(i)
if d==2:
    print("nombre permier")