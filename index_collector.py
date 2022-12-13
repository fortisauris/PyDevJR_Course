'''
I N D E X   C O L L E C T O R
'''

import importlib
modules = ['session1', 'session2']


if __name__ == '__main__':
    for i in modules:
        im = importlib.import_module(i)
        print(im.__doc__)
        print(im)
        print(type(im))
        print(id(im))
        del im