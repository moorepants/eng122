:title: Plan for Wednesday, September 21, 2016
:status: hidden

Introduction 4:10
=================

- Tell them who you are and some about you.
- Maybe show them something you've done that is related to vibrations.
- Basic explanation of what mechanical vibrations are, i.e. what you will be
  able to do at the end of the class.

Introduction activity
---------------------

- Find two people you do not already know in class.
- Tell each other your name and why this class interests you.
- Ask two or three students to share what they learned.

Class Questions 4:25
====================

- Any syllabus questions? (open up the website on the screen)

  - I'll ask them to review the syllabus and class website before arriving. So
    just ask for questions here.

- Show them Canvas (it may be new to many)
- Show them Piazza and explain how it works and that this is the primary place
  to ask questions pertaining to class. Mention that we will award points to
  top participants.
- Let them know that, in general, I'd like them to bring laptops on Wednesdays.

Engineering Computation with Python Intro 4:40
==============================================

Objectives
----------

These are the main takeaways and the things we should test them on in any of
the exercises.

- Learn the main package names and functions in the SciPy stack.
- Learn to open a Jupyter notebook and it's basic features.
- Learn the basics of Python, primarily the differences from Matlab (or C?)
- Learn how to do vectorized operations with NumPy.
- Learn to integrate a second order ODE.
- Learn to make a plot with matplotlib.
- Show how to make the plot interactive with Jupyter interact.
- Learn how to create an object and its use.
- Learn where to get help on Python.

Instructions
------------

Have the students pull out their laptops and fire up a Jupyter notebook using
Anaconda.

Windows
   Select from Start Menu
Mac and Linux
   Open terminal and type "jupyter notebook" + Enter

Go through the chosen tutorial (first chapter of scipy lecture notes) by
speaking and live coding in a notebook. Don't worry about mistakes, it's better
if they see us make mistakes. They should follow along and do what you do, them
typing is key. You should break it up with a short exercise every 15 minutes or
so. Save the notebook that you create and we will post it online for them. Be
sure to type in explanations of what you are doing for their future reference.
Be sure to take a short break some time in the middle of this tutorial.

Use sticky notes for exercises and feedback at the end.

Tell them why python:

- Easy to learn
- Very popular
- Free

Differences

- indentation matters
- You have to import everything.
- Indexing starts at 0.
- ** not ^
- etc

Here are some exercises that they can chew on during the session. They should
pair up for these:

https://github.com/moorepants/eng122/blob/master/content/materials/notebooks/exercises-01.ipynb

SciPy Lecture Notes Tutorial
============================

Cover the following topics (this is a reduced list).

1. Scientific computing with tools and workflow

   1. Why Python?

      1. The scientist’s needs
      2. Specifications
      3. Existing solutions

   2. Scientific Python building blocks
   3. *Jupyter intro here instead of IPython specific you can use http://arogozhnikov.github.io/2016/09/10/jupyter-features.html as supplement.*

2. The Python language

   1. First steps
   2. Basic types

      1. Numerical types
      2. Containers

         1. Lists
         2. Strings
         3. Dictionaries
         4. More container types

      3. Assignment operator

   3. Control Flow

      1. if/elif/else
      2. for/range
      3. while/break/continue
      4. Conditional Expressions
      5. Advanced iteration

         1. Iterate over any sequence
         2. Keeping track of enumeration number
         3. Looping over a dictionary

   4. Defining functions

      1. Function definition
      2. Return statement
      3. Parameters
      4. Skip
      5. Skip
      6. Skip
      7. Docstrings

   5. Reusing code: scripts and modules

      1. Scripts
      2. Importing objects from modules
      3. Creating modules
      4. Skip
      5. Skip
      6. Skip
      7. Good practices

   6. Input and Output

      1. Iterating over a file

         1. File modes

   7. Standard Library *Just tell them that python comes with standad libs, show one example, and how to google the others. Don't go over all of these.*
   8. Skip
   9. Object-oriented programming (OOP) *Use this example: http://nbviewer.jupyter.org/github/moorepants/eng122/blob/master/content/materials/notebooks/oo_basics.ipynb*

3. NumPy: creating and manipulating numerical data

   1. The Numpy array object

      1. What are Numpy and Numpy arrays?

         1. Numpy arrays
         2. Numpy Reference documentation
         3. Import conventions

      2. Creating arrays

         1. Manual construction of arrays
         2. Functions for creating arrays

      3. Basic data types
      4. Basic visualization
      5. Indexing and slicing
      6. Copies and views
      7. Fancy indexing

         1. Using boolean masks
         2. Indexing with an array of integers

   2. Numerical operations on arrays

      1. Elementwise operations

         1. Basic operations
         2. Other operations

      2. Basic reductions

         1. Computing sums
         2. Other reductions

      3. Broadcasting
      4. Array shape manipulation

         1. Flattening
         2. Reshaping
         3. Adding a dimension
         4. Dimension shuffling
         5. Resizing

      5. Sorting data
      6. Summary

4. Matplotlib: plotting

   1. Introduction

      1. Jupyter and the matplotlib mode *Be sure to use the "notebook" mode, not inline. This makes the graph interactive.*
      2. pyplot

   2. Simple plot

      1. Plotting with default settings
      2. Instantiating defaults
      3. Changing colors and line widths
      4. Setting limits
      5. Setting ticks
      6. Setting tick labels
      7. Moving spines
      8. Adding a legend
      9. Annotate some points
      10. Devil is in the details

   3. Figures, Subplots, Axes and Ticks

      1. Figures
      2. Subplots
      3. Axes
      4. Ticks

         1. Tick Locators

   4. Other Types of Plots: examples and exercises *Just demo making one and show them some of the others. Show them the matplotlib gallery.*

      1. Regular Plots
      2. Scatter Plots
      3. Bar Plots
      4. Contour Plots
      5. Imshow
      6. Pie Charts
      7. Quiver Plots
      8. Grids
      9. Multi Plots
      10. Polar Axis
      11. 3D Plots
      12. Text

   5. Beyond this tutorial

      1. Tutorials
      2. Matplotlib documentation
      3. Code documentation
      4. Galleries
      5. Mailing lists

   6. Quick references

      1. Line properties
      2. Line styles
      3. Markers
      4. Colormaps

5. Scipy : high-level scientific computing

    1. File input/output: scipy.io (csv and mat)
    2. SKIP
    3. Linear algebra operations: scipy.linalg
    4. Fast Fourier transforms: scipy.fftpack
    5. SKIP
    6. SKIP
    7. Interpolation: scipy.interpolate
    8. Numerical integration: scipy.integrate
    9. Signal processing: scipy.signal

6. Getting help and finding documentation *Show them stackoverflow.*

Extra Materials
===============

There are a ton of NumPy intro tutorials out there. Yet I'm still tempted to
write my on custom one for this 2 hour intro.

NumPy for Matlab Users:
http://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html

This notebook is part of the PyDy tutorial that we created and it took us 15
minutes to deliver at PyCon Montreal 2014.
http://nbviewer.jupyter.org/github/pydy/pydy-tutorial-human-standing/blob/master/notebooks/n00_python_intro.ipynb

The first chapter of SciPy Lecture notes claims to be doable in 1 to 2 hours.
http://www.scipy-lectures.org/intro/index.html

Python NumPy Tutorial (about the same content as we want)
http://cs231n.github.io/python-numpy-tutorial/

Not a fan of the latex generated stuff but might be good material:
http://math.jacobs-university.de/oliver/teaching/scipy-intro/scipy-intro.pdf

Another:
http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf

Could do first half of SWC lesson:
http://swcarpentry.github.io/python-novice-inflammation/

100 NumPy Exercises
http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html

NumPy Tutorial (really nice layout with exercises but not really appropriate
content for engineers)
http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html

NumPy Tutorial (horrible website colors)
http://www.python-course.eu/numpy.php

First Introduction to NumPy
http://www.sam.math.ethz.ch/~raoulb/teaching/PythonTutorial/intro_numpy.html

Quickstart Tutorial (SciPy Docs)
https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

Introduction to NumPy
https://www.wakari.io/nb/urls/raw.github.com/andrewgiessel/pydata_bos_2013_intro_to_numpy/master/Introduction%20To%20NumPy.ipynb?has_login=False

NumPy: lock 'n load
http://mentat.za.net/numpy/intro/intro.html

ODES
----

Nice package that has all types of ODE integrators to try out with same
interface: https://github.com/hplgit/odespy

Few other ODE packages:

- https://github.com/olivierverdier/odelab
- http://olivierverdier.github.io/odelab/
- http://www.jmodelica.org/assimulo
- https://github.com/bmcage/odes
- https://github.com/bjodah/pyodesys

Jupyter
-------

http://arogozhnikov.github.io/2016/09/10/jupyter-features.html
