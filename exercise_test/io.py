from IPython.core.display import display, HTML
import exercise_test
from exercise_test.run_exercise_magic import add_magic
import nbformat.v4 as nbf
import os
import importlib
import textwrap


def convert_exercise_to_cells(exercise):
    """
    Generates a header, exercise text and code cell from an Exercise class
    """
    cells = []
    markdown_text = "## " + exercise.name + "\n"
    markdown_text += textwrap.dedent(exercise.__doc__) or ""
    cells.append(nbf.new_markdown_cell(markdown_text))

    code_cell_text = "%%run_exercise " + exercise.name + "\n"
    code_cell_text += textwrap.dedent(exercise.cell_code)
    cells.append(nbf.new_code_cell(code_cell_text))

    return cells


def initialize(filepath):
    """
    This function should be called at the beginning of an exercise notebook to initialize everything
    """
    filepath = os.path.abspath(filepath)

    exercise_module, exercises = load_exercise_module(filepath)

    add_magic(exercises)

    css_path = os.path.join(os.path.dirname(exercise_test.__file__), "assets", "notebook_style.css")
    display(load_css(css_path))


def load_exercise_module(filepath):
    try:
        exercise_module = importlib.machinery.SourceFileLoader(
            'exercise_module', filepath
        ).load_module()
    except AttributeError:  # Python2
        import imp
        exercise_module = imp.load_source("exercise_module", filepath)

    try:
        exercises = exercise_module.exercises
    except AttributeError:
        raise NotImplementedError("For now you must define 'exercises'.")
        exercises = [
            obj for obj in exercise_module.globals().values()
            if isinstance(obj, type) and issubclass(obj, exercise_test.Exercise and obj.name is not None)
        ]
    return exercise_module, exercises


def load_css(filepath):
    """
    Return an HTML object containing the style rules from the given file
    """
    with open(filepath) as css_file:
        css_code = css_file.read()
    return HTML("<style>"+css_code+"</style>")
