# -*- coding: UTF-8 -*-
# Copyright 2014-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

# $ python setup.py test -s tests.PackagesTests.test_packages

SETUP_INFO = dict(
    name='lino-care',
    version='18.8.0',
    install_requires=['lino-xl'],
    # tests_require=['pytest', 'mock'],
    test_suite='tests',
    description=("A database for managing a network of helpers."),
    long_description="""\
.. image:: https://readthedocs.org/projects/lino/badge/?version=latest
    :alt: Documentation Status
    :target: http://lino.readthedocs.io/en/latest/?badge=latest

.. image:: https://coveralls.io/repos/github/lino-framework/care/badge.svg?branch=master
    :target: https://coveralls.io/github/lino-framework/care?branch=master

.. image:: https://travis-ci.org/lino-framework/care.svg?branch=stable
    :target: https://travis-ci.org/lino-framework/care?branch=stable

.. image:: https://img.shields.io/pypi/v/lino-care.svg
    :target: https://pypi.python.org/pypi/lino-care/

.. image:: https://img.shields.io/pypi/l/lino-care.svg
    :target: https://pypi.python.org/pypi/lino-care/

Lino Care is for managing a catalog of people who care.

- The central project homepage is http://care.lino-framework.org

- Technical documentation, including demo projects, API and tested
  specs see http://www.lino-framework.org/specs/care

- For *introductions* and *commercial information* about Lino Care
  please see `www.saffre-rumma.net
  <http://www.saffre-rumma.net/care/>`__.


""",
    author='Luc Saffre',
    author_email='luc@lino-framework.org',
    url="http://care.lino-framework.org",
    license='BSD License',
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2
Development Status :: 4 - Beta
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
Intended Audience :: System Administrators
Intended Audience :: Information Technology
Intended Audience :: Customer Service
License :: OSI Approved :: GNU Affero General Public License v3
Operating System :: OS Independent
Topic :: Software Development :: Bug Tracking
""".splitlines())

SETUP_INFO.update(packages=[str(n) for n in """
lino_care
lino_care.lib
lino_care.lib.care
lino_care.lib.care.fixtures
lino_care.lib.contacts
lino_care.lib.contacts.fixtures
lino_care.lib.public
lino_care.lib.topics
lino_care.lib.users
lino_care.lib.users.fixtures
lino_care.lib.cal
lino_care.lib.cal.fixtures
lino_care.lib.courses
lino_care.lib.tickets
""".splitlines() if n])

SETUP_INFO.update(message_extractors={
    'lino_care': [
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**.js',                'javascript', None),
        ('**/config/**.html', 'jinja2', None),
    ],
})

SETUP_INFO.update(include_package_data=True, zip_safe=False)
# SETUP_INFO.update(package_data=dict())


# def add_package_data(package, *patterns):
#     l = SETUP_INFO['package_data'].setdefault(package, [])
#     l.extend(patterns)
#     return l

# l = add_package_data('lino_care.lib.care')
# for lng in 'de fr'.split():
#     l.append('locale/%s/LC_MESSAGES/*.mo' % lng)
