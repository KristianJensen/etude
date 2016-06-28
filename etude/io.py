from IPython.core.display import display, HTML
import etude
from etude.run_exercise_magic import add_magic
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

    exercise_module = load_exercise_module(filepath)
    exercises = exercise_module.exercises

    add_magic(exercises)

    css_path = os.path.join(os.path.dirname(etude.__file__), "assets", "notebook_style.css")
    display(load_css(css_path))


def load_exercise_module(filepath):
    try:
        exercise_module = importlib.machinery.SourceFileLoader(
            'exercise_module', filepath
        ).load_module()
    except AttributeError:  # Python2
        import imp
        exercise_module = imp.load_source("exercise_module", filepath)

    return exercise_module


def load_css(filepath):
    """
    Return an HTML object containing the style rules from the given file
    """
    with open(filepath) as css_file:
        css_code = css_file.read()
    return HTML("<style>"+css_code+"</style>")
