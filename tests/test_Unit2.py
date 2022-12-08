import unittest
from unittest.mock import Mock
import sys


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


def suite():
    suite = unittest.TestSuite()  # kolekcia testov
    suite.addTest(TestMockAPI('test_msg'))
    suite.addTest(TestMockAPI('test_id'))
    return suite


if __name__ == '__main__':
    #unittest.main(verbosity=2)
    runner = unittest.TextTestRunner()
    runner.run(suite())