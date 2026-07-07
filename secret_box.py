"""
secret_box.py
-------------
DO NOT open this file until you have finished the deduction exercise in
task2_mystery_black_box/mystery_black_box.ipynb!

This module defines the hidden transformation used by the `black_box()`
function that interns are given. Peeking here defeats the purpose of the
exercise -- the whole point is to deduce this matrix using linear algebra
(specifically: feeding in the standard basis vectors), not by reading
source code.

Per the assignment brief, the black box's behavior on the standard basis
vectors has already been observed and reported to interns as:

    Inputting (1, 0) outputs (0, 1)
    Inputting (0, 1) outputs (-1, 0)

Those two observations are ALL that's needed to reconstruct the full 2x2
matrix (the columns of the matrix are exactly the images of the standard
basis vectors). This module simply implements the matrix that matches
those two reported observations, so the notebook's `black_box()` calls
behave consistently with the assignment text.
"""

from linalg import mat_vec_mul

# Column 1 = black_box(1, 0) = (0, 1)
# Column 2 = black_box(0, 1) = (-1, 0)
_SECRET_MATRIX = [
    [0, -1],
    [1, 0],
]


def black_box(point):
    """The only function interns should call. Takes a 2D point (x, y) tuple
    and returns its transformed coordinates. The transformation itself is
    fixed and hidden -- your job is to reverse-engineer it from its effect
    on the standard basis vectors, exactly as reported in the assignment."""
    return mat_vec_mul(_SECRET_MATRIX, point)
