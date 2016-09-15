The course website for Jason K. Moore's University of California, Davis
Mechanical Vibrations course (ENG 122). The rendered version can be viewed at:

http://moorepants.github.io/eng122

This site is generated with Pelican_.

.. _Pelican: getpelican.com

Build Instructions
==================

Install miniconda_. Create an environment for this website::

   $ conda create -n eng122-website python=2 pygments pip jinja2 docutils markupsafe python-dateutil pytz six unidecode fabric
   $ source activate eng122-website
   (pelican)$ pip install pelican ghp-import

Clone the plugin repository (for the render_math plugin)::

   $ mkdir ~/src
   $ git clone git@github.com:getpelican/pelican-plugins.git ~/src/

Rebuild and serve the site locally::

   (pelican)$ fab reserve

Push the site to Github pages::

   (pelican)$ fab gh_pages

.. _miniconda: http://conda.pydata.org/miniconda.html

License
=======

Creative Commons CC0

   To the extent possible under law, Jason K. Moore has waived all copyright
   and related or neighboring rights to ENG122 Mechanical Vibrations Course
   Website. This work is published from: United States.
