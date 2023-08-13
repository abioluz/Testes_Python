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


import unittest
from io import StringIO
import sys

class TestOlaMundo(unittest.TestCase):
    '''
       Objetivo é estudar uma forma de testar a saída de códigos
       Este código foi elaborado pelo chatGPT e vou manter como estudo.
    '''

    def test_ola_mundo_print(self):

        saved_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            import ola   # Importe o arquivo ola.py
            output = sys.stdout.getvalue().strip()
        finally:
            sys.stdout = saved_stdout

        # Verifica se a saída está correta
        self.assertEqual(output, "Olá Mundo")

    def test_ola_mundo_print2(self):
        # Captura a saída do print ao executar o código
        saved_stdout = sys.stdout
        try:
            sys.stdout = StringIO()

            exec(open('./src/ola.py', 'r').read())
            
            output = sys.stdout.getvalue().strip()
        finally:
            sys.stdout = saved_stdout

        # Verifica se a saída está correta
        self.assertEqual(output, "Olá Mundo")

if __name__ == '__main__':
    unittest.main()