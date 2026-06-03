print("quanti triangoli vuoi inserire?")
n=int(input())
for g in range(n):
    n1=float(input("inserisci il primo lato: "))
    n2=float(input("inserisci il secondo lato: "))
    n3=float(input("inserisci il terzo lato: "))
    if n1>n2: 
        if n1>n3:
            i=n1
            c1=n2
            c2=n3
        else:
            i=n3
            c1=n1
            c2=n2
    else:
        if n2>n3:
            i=n2
            c1=n3
            c2=n1
        else:
            i=n3
            c1=n2
            c2=n1
    f = c1**2 + c2**2
    if i**2 == f:
        print("si tratta di un triangolo rettangolo")
    else:
        print("non si tratta di un triangolo rettangolo")
