szamok=[4,7,40,44,47,70,74,77,400,404,407,440,444,447,470,474,477,700,704,707,740,744,747,770,774,777]
s=0

while True:

    try:
        n = int(input('Give a number! '))
        if n<=1000:
            for i in szamok:
                if i<n and i in szamok:
                    s+=1
            print(s)
            break


    except ValueError:
        print('The given value could not converted to number!')





