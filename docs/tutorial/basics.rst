========
 Basics
========

..
   >>> from diofant import *
   >>> x, y, z = symbols('x y z')
   >>> init_printing(pretty_print=True, use_unicode=True)

Here we discuss some of the most basic operations needed for
expression manipulation in Diofant.

Substitution
============

One of the most common things you might want to do with a mathematical
expression is substitution with :meth:`~diofant.core.basic.Basic.subs`
method.  It replaces all instances of something in an expression with
something else.

    >>> expr = cos(x) + 1
    >>> expr.subs(x, y)
    cos(y) + 1
    >>> expr
    cos(x) + 1

We see that performing substitution leaves original expression
``expr`` unchanged.

.. note::

   Almost all Diofant expressions are immutable.  No function (or
   method) will change them in-place.

To perform several substitutions in one shot, you can provide
:class:`~collections.abc.Iterable` sequence of pairs.

    >>> x**y
     y
    x
    >>> _.subs(((y, x**y), (y, x**x)))
     ⎛ ⎛ x⎞⎞
     ⎜ ⎝x ⎠⎟
     ⎝x    ⎠
    x

Use flag ``simultaneous`` to do all substitutions at once.

    >>> (x - y).subs(((x, y), (y, x)))
    0
    >>> (x - y).subs(((x, y), (y, x)), simultaneous=True)
    -x + y

Numerics
========

To evaluate a numerical expression into a floating point number with
arbitrary precision, use :meth:`~diofant.core.evalf.EvalfMixin.evalf`.
By default, 15 digits of precision are used.

    >>> expr = sqrt(8)
    >>> expr.evalf()
    2.82842712474619

But you can change that.  Let's compute the first 70 digits of `\pi`.

    >>> pi.evalf(70)
    3.141592653589793238462643383279502884197169399375105820974944592307816

Sometimes there are roundoff errors smaller than the desired precision
that remain after an expression is evaluated.  Such numbers can be
removed by setting the ``chop`` flag.

    >>> one = cos(1)**2 + sin(1)**2
    >>> (one - 1).evalf()
    -0.e-124
    >>> (one - 1).evalf(chop=True)
    0

Discussed above method is not effective enough if you intend to
evaluate an expression at many points, there are better ways,
especially if you only care about machine precision.

The easiest way to convert a Diofant expression to an expression that
can be numerically evaluated with libraries like :mod:`numpy` --- use
the :func:`~diofant.utilities.lambdify.lambdify` function.  It acts
like a :keyword:`lambda` form, except it converts the Diofant names to
the names of the given numerical library.

    >>> import numpy
    >>> a = numpy.arange(10)
    >>> expr = sin(x)
    >>> f = lambdify(x, expr, "numpy")
    >>> f(a)
    [ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
     -0.2794155   0.6569866   0.98935825  0.41211849]

You can use other libraries than NumPy. For example, the standard
library :mod:`math` module.

    >>> f = lambdify(x, expr, "math")
    >>> f(0.1)
    0.09983341664682815
