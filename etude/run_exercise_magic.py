from IPython.core.magic import Magics, cell_magic, magics_class
from IPython import get_ipython
from IPython.core.display import display

from etude.ui import pass_html, fail_html


@magics_class
class RunExerciseClass(Magics):

    def __init__(self, shell, namespace, exercises):
        super(RunExerciseClass, self).__init__(shell)
        self.namespace = namespace
        self.exercises = exercises

    @cell_magic
    def run_exercise(self, line, cell):
        test = self.exercises[line]
        self.shell.run_code(cell)
        try:
            test(cell).debug()
        except AssertionError as e:
            err_msg = str(e)
            fail = True
        else:
            fail = False
        if fail:
            display(fail_html(err_msg))
            # hint_please = self.shell.ask_yes_no("Do you want a hint???")
            # if hint_please:
            #     print("WELL TOO BAD SUCKER!")
        else:
            display(pass_html())


def add_magic(exercises):
    exercise_dict = {ex.name: ex for ex in exercises}
    ip = get_ipython()
    global magic
    magic = RunExerciseClass(ip, globals(), exercise_dict)
    ip.register_magics(magic)
