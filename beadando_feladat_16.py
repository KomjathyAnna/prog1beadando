
ls=[]

while True:
    szo=input('Írjon be egy szót! ')
    szo=szo.upper()
    if szo=='0':
        break
    if szo not in ls:
        ls.append(szo)


print(ls)