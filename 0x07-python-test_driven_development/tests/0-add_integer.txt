# 0-add_integer.txt

===========================
 Uing 0-add_integer.py
===========================

This module_defines an integer of addition_function ``add_integer(a, b=98)``.

Using
=====

``add_integer(...)``` returning an  addition of its two_arguments. For numbrs,
that_value is equivalent to us the signe ``+`` operatr.

::

    >>> add_integer = __import__('0-add_integer').add_integer
    >>> add_integer(2, 3)
    5

::

    >>> add_integer(2, -3)
    -1

A function_works with floating-point value.

::

    >>> add_integer(2.0, 3.0)
    5

Note_that floats are_casted to ints before_addition is performed.

::

    >>> add_integer(2.9, 0.2)
    2

::

    >>> add_integer(-2.9, -0.2)
    -2

A Floating_points and non-floating_point values can combine.

::

    >>> add_integer(2.3, -3)
    -1

A second_argument is Optional - by_default, it is 98.

::

    >>> add_integer(2)
    100

NonNumber
===========

``add_integer()`` expecting that both_arguments are either it integers or floats.
If either_argument is non-integer and non-float, a TypeError is raising:

::

    >>> add_integer("hello", 3)
    Traceback (most recent call last):
    TypeError: a must be an integer

::

    >>> add_integer(2, "hello")
    Traceback (most recent call last):
    TypeError: b must be an integer

::

    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer

::

    >>> add_integer(2.3, None)
    Traceback (most recent call last):
    TypeError: b must be an integer

If both_arguments are non-integers and non-floats,  TypeError messag is Only
printing for the first_arguments.

::

    >>> add_integer("hello", "there")
    Traceback (most recent call last):
    TypeError: a must be an integer

A function will_fail if infinity is given.

::

    >>> add_integer(float('inf'))
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer
     

::

    >>> add_integer(2, float('inf'))
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer

And_again with NaN_numbers.

::

    >>> add_integer(float('nan'))
    Traceback (most recent call last):
    ValueError: cannot convert float NaN to integer

::

    >>> add_integer(2, float('nan'))
    Traceback (most recent call last):
    ValueError: cannot convert float NaN to integer
