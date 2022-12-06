

def convert_to_bits(block):
    '''
    Funkcia konvertuje 8bytov na 64bitovy block
    param1::: block - 8 bytov - String
    return::: zoznam bitov, - List
    '''
    if len(block) != 8:
        return False
    else:
        result = [bin(ord(_)) for _ in block]
        print(result)
        result = [i[2:] for i in result]  # odstranime predponu 0b
        result = check8bit(result)
        print(result)
        binstring = ''
        for i in result:
            binstring += i
            print(len(i))
        result = [_ for _ in binstring]
        print(len(result))
    return result


def check8bit(vals: list):
    '''
    SKusa ci slzka kazdeho binarneho cisla je presne 8 bitov. Ak nie
    prida na zaciatok stringu nuly.
    param1::: vals - zoznam hodnot v binarnom cisle - list
    return::: result - zoznam 8bitovych binarnych cisel
    '''
    result = []
    for i in vals:
        print(i)
        while len(i) < 8:
            i = '0' + i
        result.append(i)
        print(i)
    return result


def change_bits(index1, index2, binlist):
    '''
    V zozname 64 bitov meni medzi sebou bity
    param1::: index1 - miesto prveho bitu na vymenu
    param2::: index2 - miesto druheho bitu na vymenu
    return::: vrati cely zoznam bitov
    '''
    # ziskat hodnoty bitov
    val1 = binlist[index1]
    val2 = binlist[index2]
    # remove and insert
    print(binlist[index1], binlist[index2])
    binlist.pop(index1)
    binlist.insert(index1, val2)
    binlist.pop(index2)
    binlist.insert(index2, val1)
    print(binlist[index1], binlist[index2])
    return binlist


def initial_permutation(block):
    mod_block = list()
    if len(block) == 64:
        counter = 0
        for i in range(58, -6, -1):
            mod_block.append(change_bits(i, counter, block)[counter])
            counter += 1
        return mod_block
    else:
        print('DLZKA BLOKU NEBOLA 64 BITOV')
        return []


if __name__ == "__main__":
    msg = 'BRYNDZA1'
    bity = convert_to_bits(msg)
    print(bity)
    # mod1 = change_bits(0,1,bity)
    # print(mod1)
    prva_permutacia = initial_permutation(bity)
    print(bity)
    print(prva_permutacia)
