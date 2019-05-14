
ls=[]
hossz=[]
ls_rend=[]
while True:
    szo=input('Írjon be egy szót! ')
    szo=szo.lower()
    if szo=='0':
        break
    if szo not in ls:

        ls.append(szo)

print(sorted(ls))














