:title: Plan for Wednesday, September 21, 2016
:status: hidden

Introduction 4:10
=================

- Tell them who you are and some about you.
- Maybe show them something you've done that is related to vibrations.
- Basic explanation of what mechanical vibrations are, i.e. what you will be
  able to do at the end of the class.

- Introduction activity

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

Quiz on ODEs 4:35
=================

- Hand out quiz and give them 10 minutes to complete by themselves.
- Give a show of hands for each question.
- Now give them 10 more minutes to discuss with neighbor the answers.
- Give a show of hands for each question.

Engineering Computation with Python Intro 4:45
==============================================

Objectives
----------

These are the main takeaways and the things we should test them on in any of
the exercises.

- Learn the main package names and functions in the SciPy stack.
- Learn where to get help on Python.
- Learn to open a Jupyter notebook and it's basic features.
- Learn to open Spyder and execute a script and type at the IPython interpreter.
- Learn the basics of Python, primarily the differences from Matlab (or C?)
- Learn how to do vectorized operations with NumPy.
- Learn to integrate a second order ODE.
- Learn to make a plot with matplotlib.
- Show how to make the plot interactive.
- Learn how to create an object and its use.

Instructions
------------

Have the students pull out their laptops and fire up a Jupyter notebook using
Anaconda.

Windows: Select from Start Menu
Mac and Linux: Open terminal and type "jupyter notebook" + Enter

Go through the chosen tutorial (first chapter of scipy lecture notes) by
speaking and live coding in a notebook. Don't worry about mistakes, it's better
if they see us make mistakes. They should follow along and do what you do. You
should break it up with a short exercise every 15 minutes or so. Save the
notebook that you create and we will post it online for them. Be sure to type
in explanations of what you are doing for their future reference.

Use sticky notes for exercises and feedback at the end.

Tell them why python:

- Easy to learn
- Very popular
- Free

Differences

- You have to import everything.
- Indexing starts at 0.
- ** not ^

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
interface:
https://github.com/hplgit/odespy

Few other ODE packages:
- https://github.com/olivierverdier/odelab
- http://olivierverdier.github.io/odelab/
- http://www.jmodelica.org/assimulo
- https://github.com/bmcage/odes
- https://github.com/bjodah/pyodesys
