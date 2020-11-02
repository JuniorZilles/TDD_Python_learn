"""Um exemplo do módulo de teste python"""

import unittest
from unittest.mock import patch
from module import total, join, divide, get

class TestModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """executa antes de tudo"""
        pass

    @classmethod
    def tearDownClass(cls):
        """executa ao final de tudo"""
        pass

    def setUp(self):
        """executa sempre ao inicio da execução dos testes"""
        pass

    def tearDown(self):
        """executa ao final da execução dos testes"""
        pass

    def test_total_empty(self)->None:
        """Total de lista vazia deve ser 0.0"""
        assert total([]) == 0.0

    def test_total_single_item(self) -> None:
        """Total de lista com um item é o próprio item"""
        assert total([110]) == 110.0

    def test_total_many_items(self) -> None:
        """Total de lista com mais de um item"""
        assert total([1.0,2.0,3.0]) == 6.0

    def test_join_zero_numbers(self) -> None:
        """Join of the list should bee empty"""
        assert join([], '-') == ''

    def test_join_one_item(self) -> None:
        """Join of a single item in a list should be the item itself"""
        assert join([50], '-') == '50'

    def test_join_many_items(self) -> None:
        """Join of many itens should be the list of itens joined with a delimiter eg.: 1-5-9"""
        assert join([1,2,3,4], '-') == "1-2-3-4"

    def test_join_many_items_without_delimiter(self) -> None:
        """Join of many itens should be the list of itens joined with no delimiter eg.: 159"""
        assert join([1,2,3,4], '') == "1234"

    def test_raise_error(self)->None:
        """testa se divisão por zero causa exceção"""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_request(self)->None:
        with patch('get.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            req = get('Junior')
            mocked_get.assert_called_with('http://www.compania.com/Junior/')
            self.assertEqual(req, 'Success')
