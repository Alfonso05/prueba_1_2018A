def creartxt():
    archi = open('2.txt', 'w')
    archi.close()

def grabartxt():
    archi=open('2.txt','a')
    archi.write('Inversor de contenido \n')
    archi.write('Alfonso Heredia\n\n\n')

    cad = 'hola k hace alreves'
    archi.write(cad)
    archi.write('\nCADENA INVERSA:\n')
    a = len(cad)
    for i in range(a):
        b = cad[-i - 1]
        archi.write(b)

    archi.close()



creartxt()
grabartxt()