import unittest
from unittest.mock import Mock, patch
import requests


# Função que faz uma requisição HTTP e retorna o conteúdo
def fetch_data(url):
    response = requests.get(url)
    return response.text


def process_input():
    user_input = input("Digite algo: ")
    print(f"Você digitou: {user_input}")


class TestFetchData(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        # Configura o comportamento do mock
        mock_response = Mock()
        mock_response.text = 'Dados simulados'
        mock_get.return_value = mock_response

        # Testa a função usando o mock
        result = fetch_data('http://example.com')
        self.assertEqual(result, 'Dados simulados')


class TestProcessInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['Teste de entrada'])
    @patch('builtins.print')
    def test_process_input(self, mock_print, mock_input):
        process_input()

        # Verifica se a função input foi chamada
        mock_input.assert_called_once_with('Digite algo: ')

        # Verifica se a função print foi chamada com o texto correto
        mock_print.assert_called_once_with('Você digitou: Teste de entrada')


if __name__ == '__main__':
    unittest.main()
