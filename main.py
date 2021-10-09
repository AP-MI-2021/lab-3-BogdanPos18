def printMenu():
    print("1. Citire lista")
    print("2. Determina subsecventa cu proprietatea 1")
    print("3. Determina subsecventa cu proprietatea 2")
    print("4. Iesire")


def citire_lista():
    l = []
    stringCitit = input("Dati lista: ")
    numere = stringCitit.split(",")
    for x in numere:
        l.append(int(x))
    return l


def patrat_perfect(x):
    '''
    verifica daca un nr dat este patrat perfect
    :param x: nr intreg
    :return: True, daca nr este patrat perfect, False in caz contrar
    '''
    i = 0
    while i*i < x:
        i += 1
    if i*i == x:
        return True
    return False


def test_patrat_perfect():
    assert patrat_perfect(2) is False
    assert patrat_perfect(3) is False
    assert patrat_perfect(9) is True


def toate_patrate_perfecte(list):
    '''
    verifica daca toate elementele din lista data sunt patrate perfecte
    :param list: lista de nr intregi
    :return: True, daca toate elementele din lista sunt patrate perfecte, False in caz contrar
    '''
    for x in list:
        if patrat_perfect(x) == 0:
            return False
    return True


def test_toate_patrate_perfecte():
    assert toate_patrate_perfecte([9, 16, 25]) is True
    assert toate_patrate_perfecte([2, 5, 9]) is False


def get_longest_all_perfect_squares(list):
    '''
    determina una din cele mai lungi subsecvente de nr patrate perfecte
    :param list: lista de nr intregi
    :return: una din cele mai lungi subsecvente de nr patrate perfecte
    '''
    subsecventaMax = []
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if toate_patrate_perfecte(list[i:j+1]) and len(list[i:j+1]) > len(subsecventaMax):
                subsecventaMax = list[i:j+1]
    return subsecventaMax


def test_get_longest_all_perfect_squares():
    assert (get_longest_all_perfect_squares([1, 5, 9, 16]) == [9, 16]) is True
    assert (get_longest_all_perfect_squares([2, 7, 10]) == []) is True


def bit_count(x):
    '''
    determina numarul de biti de 1 din reprezentarea binara a lui x
    :param x: nr intreg
    :return: nr de biti de 1 din reprezentarea binara a lui x
    '''
    nr = 0
    while x:
        if x % 2 == 1:
            nr += 1
        x //= 2
    return nr


def test_bit_count():
    assert (bit_count(2) == 1) is True
    assert (bit_count(15) == 3) is False


def same_bit_count(list, p):
    '''
    verifica daca elementele din lista au acelasi nr de biti de 1 in reprezentarea lor binara
    :param list: lista de nr intregi
    :param p: pozitia de la care incepe subsecventa
    :return: True, daca elementele listei au acelasi nr de biti de 1, False in caz contrar
    '''
    if p >= len(list):
        return
    for x in list:
        if bit_count(list[p]) != bit_count(x):
            return False
    return True


def test_same_bit_count():
    assert same_bit_count([1, 4, 8], 0) is True
    assert same_bit_count([7, 15], 0) is False


def get_longest_same_bit_counts(list):
    '''
    determina cea mai lunga subsecventa de nr care au acelasi nr de biti de 1
    :param list: lista de nr intregi
    :return: cea mai lunga subsecventa de nr care au acelasi nr de biti de 1
    '''
    subsecventaMax = []
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if same_bit_count(list[i:j+1], i) and len(list[i:j+1]) > len(subsecventaMax):
                subsecventaMax = list[i:j+1]
    return subsecventaMax


def test_get_longest_same_bit_counts():
    assert (get_longest_same_bit_counts([1, 4, 8, 25]) == [1, 4, 8]) is True
    assert (get_longest_same_bit_counts([3, 7, 9]) == [3, 7]) is False


def main():
    test_patrat_perfect()
    test_toate_patrate_perfecte()
    test_get_longest_all_perfect_squares()
    test_same_bit_count()
    test_get_longest_same_bit_counts()
    list = []
    while True:
        printMenu()
        optiune = input("Dati optiune: ")
        if optiune == '1':
            list = citire_lista()
        elif optiune == '2':
            print(get_longest_all_perfect_squares(list))
        elif optiune == '3':
            print(get_longest_same_bit_counts(list))
        else:
            break


main()


