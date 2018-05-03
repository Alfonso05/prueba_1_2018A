def creartxt():
    archi = open('3.txt', 'w')
    archi.close()

def leertxtenlista():
    archi=open('lista.txt','r')
    bina=archi.readlines()
    archi.close()
    return bina

def grabartxt():
    archi=open('3.txt','a')
    archi.write('codificador \n')
    archi.write('Alfonso Heredia\n\n\n')
    x = leertxtenlista()
    archi.writelines(x)
    can = len(x)
    print(x)

    cod='124'
    for i in range(can):
        for j in range (len(cod)):
            if cod[j]==can[i]:
                esc=can[i+1]
        archi.writelines(esc)


    archi.close()
grabartxt()
grabartxt()

