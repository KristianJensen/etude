from exercise_test.io import convert_exercise_to_cells, load_exercise_module
import nbformat.v4 as nbf
import argparse
import textwrap
import os

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

exercise_module, exercises = load_exercise_module(args.filename)

nb = nbf.new_notebook()

try:
    module_name = exercise_module.name
except AttributeError:
    module_name = os.path.split(os.path.splitext(args.filename)[0])[-1].capitalize()

cells = []

# Add notebook header
header_text = "# " + module_name
cells.append(nbf.new_markdown_cell(header_text))

# Add initialization (magics etc)
initialization_text = """import exercise_test
exercise_test.initialize('%s')""" % os.path.abspath(args.filename)

cells.append(nbf.new_code_cell(initialization_text))

# Add optional introduction
exercise_introduction = getattr(exercise_module, "introduction", None)
if exercise_introduction is not None:
    cells.append(nbf.new_markdown_cell(textwrap.dedent(exercise_introduction)))

# Add optional exercise-specific initialization (e.g. imports etc)
exercise_initialization_text = getattr(exercise_module, "initialization", None)
if exercise_initialization_text is not None:
    cells.append(nbf.new_code_cell(exercise_initialization_text))


# Add the exercises
for exercise in exercises:
    exercise_cells = convert_exercise_to_cells(exercise)
    cells.extend(exercise_cells)

nb.cells.extend(cells)

# write notebook
with open(os.path.splitext(args.filename)[0] + '.ipynb', 'w') as f:
    f.write(nbf.writes(nb))