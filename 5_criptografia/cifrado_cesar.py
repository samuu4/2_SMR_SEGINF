
def cifrado_cesar(cad, des):
    global abc 
    abc = list("abcdefghijklmnñopqrstuvwxyz")
    new_cad = ""

    if des >= len(abc):
        des = des % len(abc)

    for i in cad:
        if i != " ":
            pos = min(min(abc.index(i) + des, len(abc)), (abc.index(i) + des) % len(abc))
            new_cad += abc[pos]
        else:
            new_cad += " "

    return new_cad

def descifrado_cesar(cad_cif, des):
    new_cad = ""

    if des >= len(abc):
        des = des % len(abc)

    for i in cad_cif:
        if i in abc:
            pos = max(max(abc.index(i) - des, 0), (abc.index(i) - des) % len(abc))
            new_cad += abc[pos]
        else:
            new_cad += " "

    return new_cad

def cesar_fuerza_bruta(cad_cif):
    pos_cad = []
    for i in range(1, len(abc) + 1):
        pos_cad.append([i, descifrado_cesar(cad_cif, i)])

    return pos_cad

        
print(cifrado_cesar("creo que uno de los motivos mas poderosos que conducen al hombre al arte y a la ciencia es el deseo de evadirse de la vida cotidiana con su aspereza dolorosa y su vacio desesperante de escapar a las cadenas de deseos siempre cambiantes albert einstein", 15))    
print(descifrado_cesar(cifrado_cesar("hola", 3), 3))    
print(cesar_fuerza_bruta(cifrado_cesar("hola", 3)))