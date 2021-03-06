Obsolete version of Django REST framework 0.4
=============================================

**Django REST framework makes it easy to build well-connected, self-describing RESTful Web APIs.**

**Author:** Tom Christie.

Overview
========

Features:

* Creates awesome self-describing *web browse-able* APIs.
* Clean, modular design, using Django's class based views.
* Easily extended for custom content types, serialization formats and authentication policies.
* Stable, well tested code-base.
* Active developer community.

Full documentation for the project is available at http://upgrade-drf.com/docs/

Issue tracking is on `GitHub <https://github.com/upgrade-drf/django-rest-framework-0.4/issues>`_.
General questions should be taken to the `discussion group <http://groups.google.com/group/django-rest-framework>`_.

Requirements:

* Python 2.6+
* Django 1.3+


Installation Notes
==================

To clone the project from GitHub using git::

    git clone git@github.com:upgrade-drf/django-rest-framework-0.4.git


To install django-rest-framework in a virtualenv environment::

    cd django-rest-framework
    virtualenv --no-site-packages --distribute env
    source env/bin/activate
    pip install -r requirements.txt # django, coverage


To run the tests::

    export PYTHONPATH=.    # Ensure djangorestframework is on the PYTHONPATH
    python djangorestframework/runtests/runtests.py


To run the test coverage report::

    export PYTHONPATH=.    # Ensure djangorestframework is on the PYTHONPATH
    python djangorestframework/runtests/runcoverage.py


To run the examples::

    pip install -r examples/requirements.txt # pygments, httplib2, markdown
    cd examples
    export PYTHONPATH=..
    python manage.py syncdb
    python manage.py runserver


To build the documentation::

    pip install -r docs/requirements.txt   # sphinx
    sphinx-build -c docs -b html -d docs/build docs html


To run the tests against the full set of supported configurations::

    deactivate  # Ensure we are not currently running in a virtualenv
    tox


To create the sdist packages::

    python setup.py sdist --formats=gztar,zip
