'''
TDD - Test driven dvelopment (Desenvolvimento dirigido a testes)

Red
Parte 1 -> Criar o teste e ver falhar

Gren
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar meu código
'''
import unittest


# import sys
# sys.path.append(r'/home/abioluz/Documentos/Cursos/Testes_Python/')
# from src.baconcomovos import bacon_com_ovos


try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):

    def test_bco_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    def test_bco_deve_retornar_bacon_com_ovos_se_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"'
                                 )

    def test_bco_deve_retornar_passar_fome_se_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"'
                                 )

    def test_bco_deve_retornar_Bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"'
                                 )

    def test_bco_deve_retornar_Ovos_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"'
                                 )


if __name__ == '__main__':
    unittest.main(verbosity=2)
