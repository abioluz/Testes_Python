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

class TestInputOutput(unittest.TestCase):
    '''
       Objetivo é estudar uma forma de testar a saída de códigos
       Este código foi elaborado pelo chatGPT e vou manter como estudo.
    '''

    def test_input_and_print(self):

        # Simula a entrada do usuário
        user_input = "Alice\n"  # Valor que você deseja inserir

        # Redireciona a entrada padrão para o buffer
        saved_stdin = sys.stdin
        sys.stdin = StringIO(user_input)

        # Redireciona a saída padrão para outro buffer
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            # Execute o código que contém input() e print()
            exec(open('./src/input.py').read())

            # Captura a saída e a entrada simulada
            output = sys.stdout.getvalue().strip()
            input_value = sys.stdin.getvalue().strip()
        finally:
            sys.stdin = saved_stdin
            sys.stdout = saved_stdout

        # Verifica se a entrada e a saída estão corretas
        self.assertEqual(input_value, "Alice")
        self.assertIn("Digite seu nome:", output)  # Verifica se o texto está na saída
        self.assertIn("Seu nome é Alice", output)

    def test_input_and_print2(self):

        # Simula a entrada do usuário
        user_input = "Alice\n"  # Valor que você deseja inserir

        # Redireciona a entrada padrão para o buffer
        saved_stdin = sys.stdin
        sys.stdin = StringIO(user_input)

        # Redireciona a saída padrão para outro buffer
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            # Execute o código que contém input() e print()
            import input
            # Captura a saída e a entrada simulada
            output = sys.stdout.getvalue().strip()
            input_value = sys.stdin.getvalue().strip()
        finally:
            sys.stdin = saved_stdin
            sys.stdout = saved_stdout

        # Verifica se a entrada e a saída estão corretas
        self.assertEqual(input_value, "Alice")
        self.assertIn("Digite seu nome:1", output)  # Verifica se o texto está na saída
        self.assertIn("Seu nome é Alice", output)

if __name__ == '__main__':
    unittest.main()