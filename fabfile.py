from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer
import datetime

from pelican.server import ComplexHTTPRequestHandler

COURSE_NUMBER = "ENG 122"
YEAR = "2016"
QUARTER = "Fall {}".format(YEAR)
BOX_IDENTIFIER = "A"

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`clean` then `build`"""
    clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )

def gh_pages():
    """Publish to GitHub Pages"""
    clean()
    local('pelican -s publishconf.py')
    local("ghp-import -n -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))


def build_homework(num=None):
    """Collects the problems in the homework folder and constructs both a PDF
    and pelican page.

    The ``homework`` directory should contain subdirectories of two digit
    numbers, e.g. ``01``, which contain a collection of problems that are named
    as ``prob-XX.rst``. Any images should be in the same directory as the rst
    files and should be png files.

    For example::

        homework/
        |
        -> 01/
        |  |
        |  -> prob-01.rst
        |  -> prob-02.rst
        |  -> hw-01-prob-02.png
        -> 02/
        |  |
        |  -> prob-01.rst
        |  -> prob-02.rst
        |  -> hw-02-prob-01.png

    """

    hw_dir = 'homework'
    web_dir = 'content/pages/homework'
    img_dir = 'content/images'

    for d in [hw_dir, web_dir, img_dir]:
        if not os.path.exists(d):
            os.makedirs(d)

    assigned_dates = {'01': '2016/09/21',
                      '02': '2016/09/26',
                      '03': '2016/10/03',
                      '04': '2016/10/10',
                      '05': '2016/10/17',
                      '06': '2016/10/31',
                      '07': '2016/11/07',
                      '08': '2016/11/14',
                      '09': '2016/11/21'}

    due_dates = {'01': '2016/09/26',
                 '02': '2016/10/03',
                 '03': '2016/10/10',
                 '04': '2016/10/17',
                 '05': '2016/10/24',
                 '06': '2016/11/07',
                 '07': '2016/11/14',
                 '08': '2016/11/21',
                 '09': '2016/11/28'}

    pdf_header_template = """\
===============================
ENG 122 Fall 2016 Homework #{}
===============================

**DUE: {} before class in Box A in the MAE department if a paper assignment and
if digital turn it in via Canvas.**
"""

    web_header_template = """\
:title: Homework #{}
:subtitle: {}
:status: hidden

**DUE: {} before class in Box A in the MAE department if a paper assignment and
if digital turn it in via Canvas.**

`PDF Version <{{attach}}/materials/hw-{}.pdf>`_
"""
    preamble = r'\usepackage[top=1in,bottom=1in,right=1in,left=1in]{geometry}'

    rst2latex_call = ('rst2latex.py --date --documentoptions="letter,10pt"'
                      '--use-latex-docinfo --latex-preamble="{}" {} {}')

    date_format = '%A, %B %d, %Y'

    pelican_root_dir = os.path.abspath(os.path.curdir)

    if num is not None:
        hw_nums = [num]
    else:
        hw_nums = [name for name in os.listdir(hw_dir) if
                   os.path.isdir(os.path.join(hw_dir, name))]

    for hw_num in hw_nums:

        text = ""

        date_assigned = datetime.datetime.strptime(assigned_dates[hw_num],
                                                   '%Y/%m/%d')
        date_due = datetime.datetime.strptime(due_dates[hw_num], '%Y/%m/%d')

        os.chdir(os.path.join(pelican_root_dir, hw_dir, hw_num))

        contents = os.listdir(os.path.curdir)
        prob_files = [f for f in contents if f.startswith('prob-')]
        image_files = [f for f in contents if f.endswith('.png')]

        # join problem files together into a single rst file
        for p in sorted(prob_files):
            with open(p, 'r') as f:
                text += '\n'
                text += f.read()

        rst_filename = 'hw-{}.rst'.format(hw_num)
        tex_filename = 'hw-{}.tex'.format(hw_num)
        pdf_filename = 'hw-{}.pdf'.format(hw_num)

        with open(rst_filename, 'w') as f:
            hd = pdf_header_template.format(hw_num,
                                            date_due.strftime(date_format))
            f.write(hd + text)

        os.chdir(pelican_root_dir)

        with lcd(os.path.join(pelican_root_dir, hw_dir, hw_num)):
            local(rst2latex_call.format(preamble, rst_filename, tex_filename))
            local('pdflatex {}'.format(tex_filename))
            local('mv {} ../../content/materials/'.format(pdf_filename))
            local('rm hw-*.rst *.tex *.aux *.out *.log')

        # copy image files over to website
        for im_file in image_files:
            shutil.copy(os.path.join(hw_dir, hw_num, im_file), img_dir)

        with open(os.path.join(web_dir, rst_filename), 'w') as f:
            text = text.replace('.. image:: ', '.. image:: {attach}/images/')
            hd = web_header_template.format(hw_num,
                                            date_assigned.strftime(date_format),
                                            date_due.strftime(date_format),
                                            hw_num)
            f.write(hd + text)
