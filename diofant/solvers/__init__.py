"""A module for solving all kinds of equations.

    Examples
    ========

    >>> from diofant.solvers import solve
    >>> from diofant.abc import x
    >>> solve(x**5+5*x**4+10*x**3+10*x**2+5*x+1,x)
    [-1]
"""
from .solvers import (solve, solve_undetermined_coeffs,
                      solve_linear, checksol)

from .recurr import rsolve, rsolve_poly, rsolve_ratio, rsolve_hyper

from .ode import checkodesol, classify_ode, dsolve, homogeneous_order

from .polysys import solve_poly_system, solve_linear_system

from .pde import (pde_separate, pde_separate_add, pde_separate_mul,
                  pdsolve, classify_pde, checkpdesol)

from .deutils import ode_order

from .inequalities import (reduce_inequalities, reduce_piecewise_inequality,
                           reduce_piecewise_inequalities, solve_poly_inequality,
                           solve_rational_inequalities, solve_univariate_inequality)
