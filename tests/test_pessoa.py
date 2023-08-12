'''
class Pessoa:
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (inicia False)
    API:
        obter_todos_os_dados -> method
            ok
            404

        (dados_obtidos se torna True se dados obtidos com sucesso)

    conectado:
        dados_obtidos == True print('CONECTADO')
        dados_obtidos == False print('ERRO 404')

    mostrar_mensagen:
        mostra um input com "Qual a mensagem: "
        e depois printa a mensagem
'''

import unittest
from unittest.mock import patch, Mock, call
from Pessoa import Pessoa


class TestPesso(unittest.TestCase):
    def setUp(self):
        '''
            o metodo setUp inicia junto com o teste
        '''
        self.nome = 'Luiz'
        self.sobrenome = 'Otávio'
        self.p1 = Pessoa(self.nome, self.sobrenome)

    def test_pessoa_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.p1.nome, self.nome)

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_sobrenome_tem_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, self.sobrenome)

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_tem_inicial_false(self):
        self.assertFalse(self.p1.dados_obtidos)

    def test_MOCK_obter_todos_os_dados_sucess_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

    @patch('requests.get')
    def test_MOCK_obter_todos_os_dados_sucess_OK_2_patch(self, fake_request):
        fake_request.return_value.ok = True
        self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
        self.assertTrue(self.p1.dados_obtidos)

    def test_MOCK_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

    def test_MOCK_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

    def test_MOCK_conectado_print_CONECTADO(self):
        with patch('builtins.print') as fake_print, patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.p1.conectado()
            fake_print.assert_called_once_with('CONECTADO')
    
    @patch('builtins.print')
    @patch('requests.get')
    def test_MOCK_conectado_print_CONECTADO_2(self,fake_request, fake_print):
        fake_request.return_value.ok = True
        self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
        self.p1.conectado()
        fake_print.assert_called_once_with('CONECTADO')

    def test_MOCK_conectado_print_CONECTADO_3(self):
        fake_print_patch = patch('builtins.print')
        fake_request_patch = patch('requests.get')

        mock_response = Mock()
        mock_response.ok = True
        fake_request_patch.return_value = mock_response

        with fake_print_patch as fake_print, fake_request_patch as fake_request:

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.p1.conectado()
            fake_print.assert_called_once_with('CONECTADO')


    def test_MOCK_conectado_print_ERRO_404(self):
        with patch('builtins.print') as fake_print, patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.p1.conectado()
            fake_print.assert_called_once_with('ERRO 404')


    def test_MOCK_mostrar_mensagen_input_print_CONECTADO(self):
        with patch('builtins.print') as fake_print, patch('builtins.input', side_effect=['Conectado','Molhado']) as fake_input:
            self.p1.mostrar_mensagen()
            self.p1.mostrar_mensagen()
            fake_input.assert_has_calls([call('Digite a mensagem: '),
                                         call('Digite a mensagem: ')])
            fake_print.assert_has_calls([call('Conectado'),
                                         call('Molhado')])

    def test_MOCK_mostrar_mensagen_input_print_CONECTADO_2(self):
        with patch('builtins.print') as fake_print, patch('builtins.input') as fake_input:
            fake_input.side_effect=['Conectado', 'Molhado']
            self.p1.mostrar_mensagen()
            self.p1.mostrar_mensagen()
            fake_input.assert_has_calls([call('Digite a mensagem: '),
                                         call('Digite a mensagem: ')])
            fake_print.assert_has_calls([call('Conectado'),
                                         call('Molhado')])       


if __name__ == '__main__':
    unittest.main(verbosity=2)
