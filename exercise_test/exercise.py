import unittest
from IPython import get_ipython
import __main__


class Exercise(unittest.TestCase):
    _name = None
    longMessage = False
    shell = get_ipython()
    main = __main__

    cell_code = ""

    def __init__(self, cell, *args, **kwargs):
        super(Exercise, self).__init__(*args, **kwargs)
        self.cell = cell

    def runTest(self):
        pass
