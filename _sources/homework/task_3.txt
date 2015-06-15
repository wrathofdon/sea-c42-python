Homework Task 3: Explore Errors
===============================

* Create a new directory in your personal folder in the ``students`` folder of the class repository::

  $ mkdir session01
  $ cd session01

* Make sure you create it in your clone of your fork of the repository.

* Add a new file to it called ``break_me.py``

* Use ``git add`` to add the file to the repository.

.. nextslide::

* In the ``break_me.py`` file write four simple Python functions:

  * Each function, when called, should cause an exception to happen
  * Each function should result in one of the four common exceptions from our
    lecture.

    * for review: ``NameError``, ``TypeError``, ``SyntaxError``, ``AttributeError``

  * Use the Python standard library reference on `Built In Exceptions`_ as a
    reference

(hint -- the interpreter will quit when it hits a Exception -- so you can
comment out all but the one you are testing at the moment)

.. nextslide::

* Use ``git commit`` to commit changes you make to your clone

  * Make frequent, small commits using ``git commit`` when working.
  * Write clear, concise commit messages that explain what you are doing.

* When you are finished with your work, use ``git push`` to push your changes
  to your fork on GitHub.

* Finally, issue a pull request to the original CodeFellows repository with
  your work.

.. _Built In Exceptions: https://docs.python.org/2/library/exceptions.html