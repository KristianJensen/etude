import exercise_test
import re
import sys


name = "In-Silico Strain Development"

introduction = """
## Introduction

Welcome studious student,

in this small course we will teach you the basics of how to work with metabolic models in all shapes and sizes. We want to show you how easy it is ~using modern tools and packages~ to come up with design strategies for microbial production strains of the future. When we say easy we mean: "Look at me, I only needed these 100 odd lines of code to produce cumaric acid from methanol" not "Mwahaha, I just stole that baby's lolly". Although, with some practice you may find both actions equally easy, regardless of how heinous they may seem to others.

It is worth noticing that we expect you to be somewhat experienced in Python. If not, there are great tools for gaining experience:

- At [codeacademy](https://www.codecademy.com/learn/python)
- At [learnpython](http://www.learnpython.org).

Go check them out.
![alt text](http://www.relatably.com/m/img/do-it-memes/3155140.jpeg)
"""


class Lesson1(exercise_test.Exercise):
    """
    So, from [Lecture X, Slides ##-##](Link here), you know that metabolic models come in a range of different formats. You can also remember that there are several places on the web where they can reliably be obtained.

    Let's quickly recall the formats:
    - .xml aka SMBL
    - .json
    - .pickle

    And just for reference, here are the databases where a model for a bug of interest may be kept:
    - [UCSD's BiGG](http//:bigg.uscd.edu)
    - [University of Minho's GSM Database](http://darwin.di.uminho.pt/models)
    - [EMBL-EBI's BioModels Database](https://www.ebi.ac.uk/biomodels-main/)

    Cameo™ can not only import models in any of the above three formats, but it can also import models straight from the internetz, specifically from the previous two repositories, BiGG and Minho.

    #### Importing a model from the harddrive:
    To load a model from file use the command:

       ```from cameo import load_model
       load_model('PathToModel/Model.filetype')```

       1. Go ahead and try loading the latest version of the SBML-formatted genome-scale metabolic model for <i>E. coli</i>, called iJO1366 below
       2. Assign it as 'model'

       hint: The file for iJO1366 is at the following path: /core/data/blabla/
    """
    name = "Lesson 1 - Input/output"

    cell_code = "# Write your code here"

    def runTest(self):
        self.assertTrue("cameo" in sys.modules, msg="Looks like you didn't import cameo")
        self.assertTrue(re.search(r"load_model\(['\"]", self.cell), msg="You must load the model from a filepath (string)")
        self.assertTrue(hasattr(self.main, "model"), msg="Did you assign the model to the variable 'model'?")
        self.assertTrue(hasattr(self.main.model, "id") and self.main.model.id == "iJO1366", msg="The model is not iJO1366")



exercises = [Lesson1]