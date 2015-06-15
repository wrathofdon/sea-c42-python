
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.

*************************************************
Session Six: Intro to Object Oriented Programming
*************************************************

Classes, instances, attributes, and subclassing


Review/Questions
================

Review of Previous Class
------------------------

.. rst-class:: build

* Argument Passing: ``*args``, ``**kwargs``
* comprehensions
* ``lambda``
* Solutions to the FizzBuzz problem.

Homework review
---------------

* LBYL vs. EAFP

http://stackoverflow.com/questions/404795/lbyl-vs-eafp-in-java

* Line Indentations

* 

Other Homework Questions?

.. rst-class:: build
.. container::

Review of Survey Feedback
-------------------------

* Introductory readings
* More up-front explanation in class
* More connection between homework and in-class exercises
* Faster homework grading

Questions
-------------------------

* How will this prepare me for the dev accelerator?
* What about independent projects for my software portfolio?
* Do we have to worry about proper Git / GitHub technique?

Resources
-------------------------

Beginner-Friendly Textbooks

* `Interactive Python <http://interactivepython.org/runestone/static/Python-F2/index.html>`_
* `Dive Into Python <http://www.diveintopython.net/toc/index.html>`_
* `Learn Python the Hard Way <http://learnpythonthehardway.org/book/>`_

.. nextslide::

Portfolio Projects, Building Community

http://newcoder.io/

Calling Twitter APIs (thanks @mhazani!)


.. nextslide::

Preparation for Dev Accelerator Code Challenge

Django Resources

* `Tango With Django <http://www.tangowithdjango.com>`_
* `The official Django tutorial <https://docs.djangoproject.com/en/1.7/intro/tutorial01/>`_


Object Oriented Programming
===========================

.. rst-class:: left
.. container::

    Object-oriented programming narrows the "semantic gap".

    You can model real world objects with software objects.

    We'll talk more about Python implementation than OO design/strengths/weaknesses

More Detailed Reading:
----------------------

`Dive Into Python, 5.3-5.5 on Classes <http://www.diveintopython.net/object_oriented_framework/defining_classes.html>`_
`Learn Python the Hard Way <


Object Oriented Programming
---------------------------

Is Python a "True" Object-Oriented Language?

(Doesn't support full encapsulation, doesn't *require*
classes,  etc...)

.. nextslide::

.. rst-class:: center large

    I don't Care!

.. rst-class:: build
.. container::

    Good software design is about code re-use, clean separation of concerns,
    refactorability, testability, etc...

    OO can help with all that, but:
      * It doesn't guarantee it
      * It can get in the way

.. nextslide::

Python is a Dynamic Language

.. rst-class:: build
.. container::

    That clashes with "pure" OO

    Think in terms of what makes sense for your project -- not any one paradigm
    of software design.


.. nextslide::

So what is "object oriented programming"?

    Objects can be thought of as wrapping their data
    within a set of functions designed to ensure that
    the data are used appropriately, and to assist in
    that use

http://en.wikipedia.org/wiki/Object-oriented_programming

.. nextslide::

Even simpler:

.. rst-class:: build
.. container::

    "Objects are data and the functions that act on them in one place."

    This is the core of "encapsulation"

    In Python: just another namespace.

.. nextslide::

The OO buzzwords:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * data abstraction
    * encapsulation
    * modularity
    * polymorphism
    * inheritance

    Python does all of this, though it doesn't enforce them.

.. rst-class:: build
.. container::

    "OO languages" give you some handy tools to make it easier (and safer):

    .. rst-class:: build

    * polymorphism (duck typing gives you this anyway)
    * inheritance

.. nextslide::

OO has been the dominant model for the past couple decades

.. rst-class:: build
.. container::

    You will need to use it:

    - It's a good idea for a lot of problems

    - You'll need to work with OO packages

    (Even a fair bit of the standard library is Object Oriented)


.. nextslide:: Some definitions

.. rst-class:: build

class
  A category of objects: particular data and behavior: A "circle" (same as a
  type in python)

instance
  A particular object of a class: a specific circle

object
  The general case of a instance -- really any value (in Python anyway)

attribute
  Something that belongs to an object (or class): generally thought of as a
  variable, or single object, as opposed to a ...

method
  A function that belongs to a class

.. nextslide::

.. rst-class:: center large

    Note that in python, functions are first class objects, so a method *is* an
    attribute

Python Classes
==============

.. rst-class:: left
.. container::

    The ``class``  statement

    .. rst-class:: build
    .. container::

        ``class``  creates a new type object:

        .. code-block:: ipython

            In [4]: class C(object):
               ...:     pass
               ...:
            In [5]: type(C)
            Out[5]: type

        A class is a type -- interesting!

        It is created when the statement is run -- much like ``def``

        You don't *have* to subclass from ``object``, but you *should*

        (note on "new style" classes)


Python Classes
--------------

About the simplest class you can write

.. code-block:: python

    >>> class Point(object):
    ...     x = 1
    ...     y = 2
    >>> Point
    <class __main__.Point at 0x2bf928>
    >>> Point.x
    1
    >>> p = Point()
    >>> p
    <__main__.Point instance at 0x2de918>
    >>> p.x
    1

.. nextslide::

Basic Structure of a real class:

.. code-block:: python

    class Point(object):
        # everything defined in here is in the class namespace

        def __init__(self, x, y):
            # everything attached to self is in the instance namespace
            self.x = x
            self.y = y

    ## create an instance of the class
    p = Point(3,4)

    ## access the attributes
    print "p.x is:", p.x
    print "p.y is:", p.y


see: ``Examples/Session06/simple_classes.py``

.. nextslide:: The Initializer

The ``__init__``  special method is called when a new instance of a class is
created.

.. rst-class:: build
.. container::

    You can use it to do any set-up you need

    .. code-block:: python

        class Point(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y


    It gets the arguments passed when you *call* the class object:

    .. code-block:: python  

        Point(x, y)

.. nextslide:: ``self``

What is this ``self`` thing?

.. rst-class:: build
.. container::

    The instance of the class is passed as the first parameter for every method.

    Using ``self`` is only a convention -- but you DO want to use it.

    .. code-block:: python

        class Point(object):
            def a_function(self, x, y):
        ...

    Does this look familiar from C-style procedural programming?


.. nextslide:: The Instance Namespace

Anything assigned to a ``self.<xyz>``  attribute is kept in the *instance*
name space -- ``self`` *is* the instance.

.. rst-class:: build
.. container::

    That's where all the instance-specific data is.

    .. code-block:: python

        class Point(object):
            size = 4
            color= "red"
            def __init__(self, x, y):
                self.x = x
                self.y = y

.. nextslide:: The Class Namespace

Anything assigned in the class scope is a class attribute

.. rst-class:: build
.. container::

    Every *instance* of the class shares the same one.

    Note: the methods defined by ``def`` are class attributes as well.

    .. container::
    
        The class is one namespace, the instance is another.

        .. code-block:: python  

            class Point(object):
                size = 4
                color= "red"
            ...
                def get_color():
                    return self.color
            >>> p3.get_color()
             'red'

    Class attributes are accessed with ``self``  also.


.. nextslide:: Class Methods

Typical methods:

.. rst-class:: build
.. container::

    .. code-block:: python  

        class Circle(object):
            color = "red"

            def __init__(self, diameter):
                self.diameter = diameter

            def grow(self, factor=2):
                self.diameter = self.diameter * factor


    Methods take some parameters, manipulate the attributes in ``self``.

    They may or may not return something useful.

.. nextslide:: Gotcha!

.. code-block:: python

    ...
        def grow(self, factor=2):
            self.diameter = self.diameter * factor
    ...
    In [205]: C = Circle(5)
    In [206]: C.grow(2,3)

    TypeError: grow() takes at most 2 arguments (3 given)

.. rst-class:: build
.. container::

    Huh???? I only gave 2

    ``self`` is implicitly passed in for you by python.

    (demo of bound vs. unbound methods)

.. nextslide::

Using ``self`` explicitly like this can seem a bit confusing

.. rst-class:: build
.. container::

    But like most of Python's quirks, there's a rationale behind it

    Our BDFL has made the decision that ``self`` will stay, and written
    extensively about why:

    http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html

LAB / Homework
--------------

Let's say you need to render some html..

.. rst-class:: build
.. container::

    The goal is to build a set of classes that render an html page.

    ``Examples/Session06/sample_html.html``

    We'll start with a single class, then add some sub-classes to specialize the behavior

    Details in:

    :ref:`homework_html_renderer`

    Let's see if we can do step 1. in class...

Subclassing/Inheritance
=======================

Inheritance
-----------

In object-oriented programming (OOP), inheritance is a way to reuse code of
existing objects, or to establish a subtype from an existing object.


Objects are defined by classes, classes can inherit attributes and behavior
from pre-existing classes called base classes or super classes.

The resulting classes are known as derived classes or subclasses.

(http://en.wikipedia.org/wiki/Inheritance_%28object-oriented_programming%29)

Subclassing
-----------

A subclass "inherits" all the attributes (methods, etc) of the parent class.

You can then change ("override") some or all of the attributes to change the
behavior.

You can also add new attributes to extend the behavior.

The simplest subclass in Python:

.. code-block:: python

    class A_subclass(The_superclass):
        pass

``A_subclass``  now has exactly the same behavior as ``The_superclass``

NOTE: when we put ``object`` in there, it means we are deriving from object --
getting core functionality of all objects.

Overriding attributes
---------------------

Overriding is as simple as creating a new attribute with the same name:

.. code-block:: python

    class Circle(object):
        color = "red"

    ...

    class NewCircle(Circle):
        color = "blue"
    >>> nc = NewCircle
    >>> print nc.color
    blue


all the ``self``  instances will have the new attribute.

Overriding methods
------------------

Same thing, but with methods (remember, a method *is* an attribute in python)

.. code-block:: python

    class Circle(object):
    ...
        def grow(self, factor=2):
            """grows the circle's diameter by factor"""
            self.diameter = self.diameter * factor
    ...

    class NewCircle(Circle):
    ...
        def grow(self, factor=2):
            """grows the area by factor..."""
            self.diameter = self.diameter * math.sqrt(2)


all the instances will have the new method

.. nextslide::

A Program Design Suggestion:

    whenever you override a method, the interface of the new method should be
    the same as the old.  It should take the same parameters, return the same
    type, and obey the same preconditions and postconditions.

.. nextslide::

A Program Design Suggestion

    If you obey this rule, you will find that any function designed to work
    with an instance of a superclass, like a Deck, will also work with
    instances of subclasses like a Hand or PokerHand.  If you violate this
    rule, your code will collapse like (sorry) a house of cards.

    -- [ThinkPython 18.10]

( Demo of class vs. instance attributes )


More on Subclassing
===================

Overriding ``__init__``
-----------------------

Wanting or needing to override ``__init__`` is very common

.. rst-class:: build
.. container::

    You often need to call the super class ``__init__``  as well

    Think "everything the parent does, plus this stuff too"

    .. code-block:: python

        class Circle(object):
            color = "red"
            def __init__(self, diameter):
                self.diameter = diameter
        ...
        class CircleR(Circle):
            def __init__(self, radius):
                diameter = radius*2
                Circle.__init__(self, diameter)

    exception to: "don't change the method signature" rule.

More subclassing
----------------

You can also call the superclass' other methods:

.. code-block:: python  

    class Circle(object):
    ...
        def get_area(self, diameter):
            return math.pi * (diameter/2.0)**2


    class CircleR2(Circle):
    ...
        def get_area(self):
            return Circle.get_area(self, self.radius*2)

There is nothing special about ``__init__``  except that it gets called
automatically when you instantiate an instance.


When to Subclass
----------------

.. rst-class:: build
.. container::

    "Is a" relationship: Subclass/inheritance

    "Has a" relationship: Composition

.. nextslide::

"Is a" vs "Has a"

.. rst-class:: build
.. container::

    You may have a class that needs to accumulate an arbitrary number of
    objects.

    A list can do that -- so should you subclass list?

    Ask yourself:

    -- **Is** your class a list (with some extra functionality)?

    or

    -- Does you class **have** a list?

    You only want to subclass list if your class could be used anywhere a list can
    be used.

Attribute resolution order
--------------------------

When you access an attribute:

``An_Instance.something``

Python looks for it in this order:

.. rst-class:: build

* Is it an instance attribute?
* Is it a class attribute?
* Is it a superclass attribute?
* Is it a super-superclass attribute?
* ...

.. rst-class:: build
.. container::

    It can get more complicated...

    http://www.python.org/getit/releases/2.3/mro/

    http://python-history.blogspot.com/2010/06/method-resolution-order.html


What are Python classes, really?
--------------------------------

Putting aside the OO theory...

.. rst-class:: build
.. container::

    Python classes are:

    .. rst-class:: build

    * Namespaces

      * One for the class object
      * One for each instance

    * Attribute resolution order
    * Auto tacking-on of ``self`` when methods are called

    That's about it -- really!

Type-Based dispatch
-------------------

You'll see code that looks like this:

.. code-block:: python

      if isinstance(other, A_Class):
          Do_something_with_other
      else:
          Do_something_else

.. rst-class:: build
.. container::

    Usually better to use "duck typing" (polymorphism)

    But when it's called for:

    .. rst-class:: build

    * ``isinstance()``
    * ``issubclass()``

.. nextslide::

GvR: "Five Minute Multi- methods in Python":

http://www.artima.com/weblogs/viewpost.jsp?thread=101605

http://www.python.org/getit/releases/2.3/mro/

http://python-history.blogspot.com/2010/06/method-resolution-order.html


Wrap Up
-------

Thinking OO in Python:

.. rst-class:: build
.. container::

    Think about what makes sense for your code:

    .. rst-class:: build

    * Code re-use
    * Clean APIs
    * ...

    Don't be a slave to what OO is *supposed* to look like.

    Let OO work for you, not *create* work for you

.. nextslide:: OO in Python:

.. rst-class:: build
.. container::

    .. container::

        **The Art of Subclassing**: *Raymond Hettinger*

        http://pyvideo.org/video/879/the-art-of-subclassing

        "classes are for code re-use -- not creating taxonomies"

    .. container::

        **Stop Writing Classes**: *Jack Diederich*

        http://pyvideo.org/video/880/stop-writing-classes

        "If your class has only two methods and one of them is ``__init__``,
        you don't need a class"

Homework
========

Task 17: HTML Renderer
----------------------

.. rst-class:: left
.. container::

    Build an html rendering system:

    :ref:`homework_html_renderer`

    You will build an html generator, using:

    * A Base Class with a couple methods
    * Subclasses overriding class attributes
    * Subclasses overriding a method
    * Subclasses overriding the ``__init__``

    These are the core OO approaches

Create a directory called ``session06`` in your student directory.
Create a branch in your local repo called `task17` and switch to it (`git checkout -b task17`).

Add your files
to that branch, commit frequently, and push to it as you work,
writing good commit messages.
Then create a pull request to the main class repo,
titled ``Task 17 pull request from Your Name`` where you should substitute your name for ``Your Name``.

Task 18: Investigate Session 7
------------------------------

Read through the Session 7 slides.

http://codefellows.github.io/sea-c34-python/session07.html

There are five sections. For each one, come up with one question.

* Testing (1 question)
* Multiple Inheritance (1 question)
* Properties (1 question)
* Class and Static Methods (1 question)
* Special (Magic) Methods (1 question)

Write some
Python code to answer these questions, one function per question.

For each function, write a good ``docstring`` describing what
question you are trying to answer.

Put the functions in four separate modules (files) called
`testing.py`, `multiple.py`, `properties.py`, `static.py`, and
`special.py` in the
``session06`` subdirectory of your student directory.

.. nextslide::

That is, you should have seven questions, and seven functions, total,
spread out across three files.

You may use everything you've learned
so far as needed (including lists, tuples, slicing, iteration, functions, booleans, printing, modules, assertions, dictionaries,
sets, exceptions, file reading/writing, paths, lambdas, keyword/variable arguments, comprehensions, and object-oriented programming).

Create a branch in your local repo called `task18` and switch to it (`git checkout task18`).

Add your files
to that branch, commit and push, then create a pull request to
the main class repo,
titled ``Task 18 pull request from Your Name`` where you should substitute your name for ``Your Name``.

Finally, submit your assignment in Canvas by giving the URL of the pull request.
