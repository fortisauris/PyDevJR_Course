import unittest
from unittest.mock import Mock
import sys
import vstupy.rychlomer



mock = Mock()
mock.api.return_value = {
    'id': 7643643,
    'msg': 'Au'
}

class TestMockAPI(unittest.TestCase):

    @unittest.skip(reason='LEBO JE ZBYTOCNY')
    def test_response(self):
        self.assertEqual(mock.api(), {'id': 7643643,'msg': 'Au'})

    @unittest.skipIf(sys.version.startswith('3.9.13'), 'NOT SUPPORTED')
    def test_response_type(self):
        self.assertEqual(type(mock.api()), dict)

    @unittest.skipUnless(sys.platform.startswith('linux'), 'POTREBUJE LINUX')
    def test_id(self):
        if mock.api()['id'] == 0:
            self.skipTest('ZBYTOCNE')
        self.assertTrue(str(mock.api()['id']).isdigit())
        self.assertEqual(type(mock.api()['id']), int, msg='Ahoj z Unittestu')

    def test_msg(self):
        self.assertFalse(str(mock.api()['msg']).isdigit())
        self.assertEqual(type(mock.api()['msg']), str, msg='Ahoj z Unittestu')


class TestVystraha(unittest.TestCase):

    def test_vystraha_normal(self):
        vstupy.rychlomer.rychlost = Mock()
        vstupy.rychlomer.rychlost.return_value = 50
        self.assertFalse(vstupy.rychlomer.vystraha())

    def test_vystraha_vyssia(self):
        vstupy.rychlomer.rychlost = Mock()
        vstupy.rychlomer.rychlost.return_value = 130
        self.assertTrue(vstupy.rychlomer.vystraha())

    def test_vystraha_nizsia(self):
        vstupy.rychlomer.rychlost = Mock()
        vstupy.rychlomer.rychlost.return_value = 25
        self.assertTrue(vstupy.rychlomer.vystraha())

def suite():
    suite = unittest.TestSuite()  # kolekcia testov
    suite.addTest(TestMockAPI('test_msg'))
    suite.addTest(TestMockAPI('test_id'))
    return suite


if __name__ == '__main__':
    #unittest.main(verbosity=2)
    runner = unittest.TextTestRunner()
    runner.run(suite())