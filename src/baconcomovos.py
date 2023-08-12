'''
1 - Receber um númeor inteiro
2 - Saber se o númeor é multiplo de 3 e 5:
    Bacon com ovos
3 - Saber se o númeor é multiplo somente de 3:
    Bacon
4 - Saber se o númeor é multiplo somente de 5:
    Ovos
5 - Saber o número NÃO é multiplo de 3 e 5:
    Passar fome

'''


def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    elif n % 3 == 0:
        return 'Bacon'
    elif n % 5 == 0:
        return 'Ovos'
    else:
        return 'Passar fome'
