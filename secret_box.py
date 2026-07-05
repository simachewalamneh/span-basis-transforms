"""
secret_box.py
-------------
DO NOT open this file until you have finished the deduction exercise in
task2_mystery_black_box/mystery_black_box.ipynb!

This module defines the hidden composite transformation used by the
`black_box()` function that interns are given. Peeking here defeats the
purpose of the exercise -- the whole point is to deduce this matrix using
linear algebra (specifically: feeding in the standard basis vectors),
not by reading source code.
"""

from linalg import rotation_matrix, scaling_matrix, shear_matrix, reflection_matrix, compose, mat_vec_mul

# The secret is a composition of THREE elementary transformations, applied
# in this order (rightmost first, matching function composition notation):
#
#   1. A shear                (applied first)
#   2. A non-uniform scale    (applied second)
#   3. A rotation             (applied last)
#
# i.e. secret_point = Rotate( Scale( Shear( point ) ) )
#
# Order matters! Swapping the order of these three would produce a
# different composite matrix, since matrix multiplication is not commutative.

_SHEAR = shear_matrix(kx=0.5, ky=0)
_SCALE = scaling_matrix(sx=2, sy=1)
_ROTATE = rotation_matrix(theta_degrees=30)

_SECRET_MATRIX = compose(_ROTATE, _SCALE, _SHEAR)


def black_box(point):
    """The only function interns should call. Takes a 2D point (x, y) tuple
    and returns its transformed coordinates. The transformation itself is
    fixed and hidden -- your job is to reverse-engineer it."""
    return mat_vec_mul(_SECRET_MATRIX, point)
