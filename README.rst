============
django-reset
============

This is a port of Django's ``reset`` management command that was shipped with
Django 1.4.x and earlier. Django 1.5 removed this command.

There might be good reasons not to further maintain it in the Django core,
however it was always quite useful during prototyping a new Django based
project. Thats why I decided to bring it to Django 1.5 and higher with this
app.

Full credits for the code goes to the awesome Django project.

Installation
============

1. Install ``django-reset`` with pip::
    
    pip install django-reset

2. Add ``'django_reset'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'django_reset',
        ...
    )

Usage
=====

django-admin.py reset <appname appname ...>
-------------------------------------------

Executes the equivalent of ``sqlreset`` for the given app name(s).

The ``--noinput`` option may be provided to suppress all user prompts.

The ``--database`` option can be used to specify the alias
of the database to reset.

django-admin.py sqlreset <appname appname ...>
----------------------------------------------

Prints the DROP TABLE SQL, then the CREATE TABLE SQL, for the given app
name(s).

The ``--database`` option can be used to specify the database for which to
print the SQL.

Trivia
======

For code, bug reports, patches or if you wish to contact me, go to
https://github.com/gregmuellegger/django-reset
