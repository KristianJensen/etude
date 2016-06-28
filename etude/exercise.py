import unittest
import six
from IPython import get_ipython
import __main__


class ExerciseMeta(type):
    _exercises = []

    def __new__(mcs, name, bases, attrs):
        cls = super(ExerciseMeta, mcs).__new__(mcs, name, bases, attrs)
        if attrs.get("_name", None) is not None:
            mcs._exercises.append(cls)
        return cls


@six.add_metaclass(ExerciseMeta)
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

exercises = ExerciseMeta._exercises