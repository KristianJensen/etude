import etude


class Exercise1(etude.Exercise):
    """
    Define a function that sorts an input list.
    """
    name = "Exercise 1"

    cell_code = """
        def sort_function(li):
            pass # define your function here
    """

    def runTest(self):
        self.assertFalse("sorted(" in self.cell, msg="You cheated :( Don't use 'sorted()'")
        li = [2, 6, 9, 3, 10]
        self.assertEqual(self.main.sort_function(li), sorted(li), "The list is not sorted.")


exercises = [Exercise1]
