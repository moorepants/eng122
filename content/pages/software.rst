:title: Software
:sortorder: 3

We will be using a custom Python package named resonance_ during the class to
investigate a variety of mechanically vibrating systems. Resonance is an open
source software package developed by the instructors and is built on top of the
`Scientific Python`_ ecosystem of software packages.

.. _resonance: https://github.com/moorepants/resonance
.. _Scientific Python: https://scipy.org/

The documentation for resonance can be found at:

http://resonance.readthedocs.io

The rendered Jupyter notebooks that are used in class can be found at:

https://moorepants.github.io/resonance/

Finally, the source code for resonance can be found at:

https://github.com/moorepants/resonance

Running The Software
====================

The easiest, and preferred method, of running the software is to log into
http://bicycle.ucdavis.edu with your UCD email address to access our JupyterHub
server. You can then either create a new terminal session or a "Python 3"
Jupyter notebook. We will primarily be using Jupyter notebooks in class.

Backing Up Your Work
--------------------

The JupyterHub server has an automated backup in place should any problems
occur, but it is recommended to regularly back up your own work. To do so,
open a terminal from the JupyterHub interface (go to ``New -> Terminal``). From
this terminal window, type ``backup-home``. This will find all of your files
and put them in a zip file called ``backup.zip``, which you should then be able
to see and download from JupyterHub interface. Any time you want to back up
your work, you can run this command again from the terminal and it will add any
new or changed files to the zip file on the server (you have to download it to
your own computer each time).

Installing the Software On Your Personal Computer
=================================================

If you want to run the software locally on your own computer, you can install
the same packages that we have on the server. We recommend that you first
install the Anaconda_ distribution of Python which includes most all of the
packages you will need.

.. _Anaconda: https://www.anaconda.com/download/

With this, you can open up either Jupyter notebooks or use the Spyder IDE
(which also can open notebooks).

Currently, you will need to install resonance via the command line tool
``pip``. Open a terminal on Mac OSX or Linux or an Anconda Command Prompt on
Windows and type::

   pip install resonance

To upgrade resonance as we release new versions, type::

   pip install -U resonance

Learning Python For Engineering Computation
===========================================

These are my recommended resources:

- The SciPy Lecture Notes: http://www.scipy-lectures.org/
- Effective Computation in Physics Anthony Scopatz & Kathryn Huff
  http://physics.codes/
- https://stackoverflow.com/ (Q & A site, search for topics of interest)

Each software package also has documentation:

- Jupyter: http://jupyter.org/documentation.html
- NumPy: https://docs.scipy.org/doc/numpy/
- matplotlib: https://matplotlib.org/contents.html
- SciPy: https://docs.scipy.org/doc/scipy/reference/
- Pandas: https://pandas.pydata.org/pandas-docs/stable/
- SymPy: http://docs.sympy.org/latest/index.html

For beginning Python, I recommend ThinkPython_ by Allen Downey.

.. _ThinkPython: http://greenteapress.com/wp/think-python/

There are thousands of other online resources that cover the full spectrum of
using Python for scientific and engineering computing.

Example Notebooks
=================

To get an idea of what you can do with Jupyter notebooks, here are some
examples:

- https://nbviewer.jupyter.org/
- A tutorial I gave at SciPy 2017: http://www.sympy.org/scipy-2017-codegen-tutorial/
- The PyDy Human Standing Tutorial: https://github.com/pydy/pydy-tutorial-human-standing
- CFDPython: https://github.com/barbagroup/CFDPython
- Notebook gallery: http://nb.bianp.net/sort/views/
