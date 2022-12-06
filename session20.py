
# Pokracujeme v Obalke

#  POKARACUJEME OPXLS_Formatovanie.py

def line_intersection(line1, line2):  # ((bod1,bod2)(bod1,bod2))
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return x, y


#a = line_intersection(((0, 0), (100, 100)), ((100, 0), (0, 100)))
# print(a)

# TODO Chcem aby ste okomentovali kazdy riadok a popisali co sa v algoritme deje.

# TODO Prestavka do 20:10

'''     P R I P R A V A   64 bitoveho B L O C K U na sifrovanie DES    '''
# length = 64 / 8  #   8 znakov


def convert_to_bits(block):
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
    result = []
    for i in vals:
        print(i)
        while len(i) < 8:
            i = '0' + i
        result.append(i)
        print(i)
    return result


def change_bits(index1, index2, binlist):
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


def test_change_bits():
    assert change_bits(0,7, [0,0,0,0,0,0,0,1])  == [1,0,0,0,0,0,0,0]
    assert change_bits(1, 2, [1, 1, 0, 1]) == [1, 0, 1, 1]


def test_check8bit():
    assert check8bit(['1111']) == ['00001111']


if __name__ == '__main__':
    binlist = convert_to_bits('BRYNDZA!')
    print(binlist)


