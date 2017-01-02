

def bin_to_decimal(nbr) :
    return int(nbr, 2)

def is_binary(chaine) :
    if len(chaine) < 8 :
        return 0
    res = 1

    for f in chaine :
        if f != "1" and f != "0" :
            res = 0
            break
    return res

def chaine_to_mots(chaine) :
    res = []
    tmp = ""
    for f in range(1,len(chaine)+1) :
        if not f%8 :
            tmp = tmp + chaine[f-1]
            res.append(tmp)
            tmp = ""
        else :
            tmp = tmp + chaine[f-1]
    return res



def mots_to_lettre(mot) :
    return chr(int(mot, 2))

def convert_from_ascii(chaine) :
    ch = chaine_to_mots(chaine)
    res = ""
    for f in ch :
        res = res + str(mots_to_lettre(f))
    return res




a = "0111111111111110"

print(is_binary(a))
print(chaine_to_mots(a))
print(convert_from_ascii("010000100110111101101110011011100110010100100000011010010110010001100101011001010010000000100001"))