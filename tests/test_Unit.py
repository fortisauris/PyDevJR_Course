import unittest
from unittest.mock import Mock, MagicMock
import pytest
from session22 import give_me_five, get_status

mock = Mock()
mock.__str__ = Mock(return_value='BRYNDZAZDRAZELA')

class TestStringMethods(unittest.TestCase):

    @pytest.mark.string
    def test_upper(self):
        self.assertEqual('bryndza'.upper(), 'BRYNDZA')

    @pytest.mark.string
    def test_isupper(self):
        self.assertTrue('BRYNDZA'.isupper())

    def test_split(self):
        s = 'Hello World'
        self.assertEqual(s.split(' '), ['Hello', 'World'])
        with self.assertRaises(TypeError):
            s.split(2)


class TestGiveMeFive(unittest.TestCase):

    def test_response(self):
        self.assertEqual(give_me_five(), 5)

    def test_status(self):
        self.assertTrue(get_status())

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            print(give_me_five()/0)

class TestMockObject(unittest.TestCase):

    def test_mockingstring(self):
        self.assertEqual(mock.__str__(), 'BRYNDZAZDRAZELA')

# TODO Prestavka do 20:10


if __name__ == '__main__':
    unittest.main()