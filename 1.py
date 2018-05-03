def creartxt():
    archi = open('1.txt', 'w')
    archi.close()

def leertxtenlista():
    archi=open('binario.txt','r')
    bina=archi.readlines()
    archi.close()
    return bina

def grabartxt():
    archi=open('1.txt','a')
    archi.write('NUMEROS BINARIOS \n')
    archi.write('Alfonso Heredia\n\n\n')

    x = leertxtenlista()
    archi.writelines(x)
    can = len(x)
    deci = 0

    for i in range(can):
        op = int(x[-i - 1])
        ex = 2 ** i
        deci = deci + (ex * op)

    archi.writelines('\nresultado= ')

    print(deci)

    archi.close()



creartxt()
grabartxt()