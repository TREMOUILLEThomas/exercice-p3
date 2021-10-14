a=int(input("entre la première longueur du triangle:"))
b=int(input("entre la deuxième longueur du triangle:"))
c=int(input("entre la troisième longueur du triangle:"))

if a==b==c:
    print("triangle équilateral")
elif a==b:
    print("triangle isocèle")
elif a==c:
    print("triangle isocèle")
elif b==c:
    print("trianle isocèle")
elif a!=b!=c:
    print("triangle scalène")
    
