"""
linalg.py
---------
A tiny linear algebra library built from scratch using only core Python
(lists, tuples, the `fractions` module for exact arithmetic).

NO numpy. NO scipy. This is the whole point of the exercise: interns should
see exactly what determinants, rank, span, basis, and matrix transforms
*are*, mechanically, instead of calling a black-box library function.

Conventions
-----------
- A "vector" is a tuple of numbers, e.g. (1, 2).
- A "matrix" is a list of rows, e.g. [[1, 2], [3, 4]] is
        | 1  2 |
        | 3  4 |
  Column vectors passed into a matrix (e.g. as movement vectors) are stored
  as columns using `columns_to_matrix`.
"""

from fractions import Fraction


# ---------------------------------------------------------------------------
# Basic vector operations
# ---------------------------------------------------------------------------

def vec_add(v1, v2):
    return tuple(a + b for a, b in zip(v1, v2))


def vec_sub(v1, v2):
    return tuple(a - b for a, b in zip(v1, v2))


def scalar_mult(c, v):
    return tuple(c * a for a in v)


def dot(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))


# ---------------------------------------------------------------------------
# Matrix construction / basic ops
# ---------------------------------------------------------------------------

def columns_to_matrix(cols):
    """Build a matrix from a list of column vectors."""
    n_rows = len(cols[0])
    return [[cols[c][r] for c in range(len(cols))] for r in range(n_rows)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    """Multiply matrix A (m x n) by matrix B (n x p) -> (m x p)."""
    n = len(B)
    p = len(B[0])
    m = len(A)
    result = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return result


def mat_vec_mul(A, v):
    """Multiply matrix A by column vector v (tuple) -> tuple."""
    return tuple(sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A)))


def identity(n):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]


# ---------------------------------------------------------------------------
# Determinant (general, via cofactor expansion -- works for any n x n,
# but we mainly use it for 2x2 and 3x3 in these exercises)
# ---------------------------------------------------------------------------

def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    total = 0
    for col in range(n):
        minor = [row[:col] + row[col + 1:] for row in A[1:]]
        sign = 1 if col % 2 == 0 else -1
        total += sign * A[0][col] * det(minor)
    return total


# ---------------------------------------------------------------------------
# Row reduction / rank (Gaussian elimination, exact via Fraction)
# ---------------------------------------------------------------------------

def to_fraction_matrix(A):
    return [[Fraction(x) for x in row] for row in A]


def rref(A):
    """Reduced row echelon form. Returns a new matrix, does not mutate A."""
    M = to_fraction_matrix(A)
    rows, cols = len(M), len(M[0])
    pivot_row = 0
    for col in range(cols):
        # find a pivot
        pivot = None
        for r in range(pivot_row, rows):
            if M[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
       #swape two rows
        M[pivot_row], M[pivot] = M[pivot], M[pivot_row]
       #multiply row with none zeno costant
        piv_val = M[pivot_row][col]
        M[pivot_row] = [x / piv_val for x in M[pivot_row]]
       #add/substract one row with multiple of another row 
        for r in range(rows):
            if r != pivot_row and M[r][col] != 0:
                factor = M[r][col]
                M[r] = [a - factor * b for a, b in zip(M[r], M[pivot_row])]
        #advancing
        pivot_row += 1
        if pivot_row == rows:
            break
    return M


def rank(A):
    R = rref(A)
    return sum(1 for row in R if any(x != 0 for x in row))


def is_linearly_independent(vectors):
    """vectors: list of tuples, all the same length."""
    A = columns_to_matrix(vectors)
    return rank(A) == len(vectors)


def spans_r2(vectors):
    """True if the given vectors (as R^2 vectors) span all of R^2."""
    A = columns_to_matrix(vectors)
    return rank(A) == 2


# ---------------------------------------------------------------------------
# Number theory helpers (for the integer-lattice reachability problem)
# ---------------------------------------------------------------------------

def egcd(a, b):
    """Extended Euclidean algorithm. Returns (g, x, y) with a*x + b*y = g."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def gcd(a, b):
    g, _, _ = egcd(a, b)
    return abs(g)


# ---------------------------------------------------------------------------
# 2D transformation matrix builders (for the Mystery Black Box task)
# ---------------------------------------------------------------------------

import math


def rotation_matrix(theta_degrees):
    theta = math.radians(theta_degrees)
    c, s = math.cos(theta), math.sin(theta)
    return [[c, -s], [s, c]]


def scaling_matrix(sx, sy):
    return [[sx, 0], [0, sy]]


def reflection_matrix(axis="x"):
    if axis == "x":
        return [[1, 0], [0, -1]]
    if axis == "y":
        return [[-1, 0], [0, 1]]
    if axis == "origin":
        return [[-1, 0], [0, -1]]
    if axis == "y=x":
        return [[0, 1], [1, 0]]
    raise ValueError("axis must be one of 'x', 'y', 'origin', 'y=x'")


def shear_matrix(kx=0, ky=0):
    return [[1, kx], [ky, 1]]


def compose(*matrices):
    """Compose transformations. compose(A, B, C) applied to a point means
    A(B(C(point))) -- i.e. rightmost matrix is applied FIRST, matching the
    usual mathematical convention for function composition."""
    result = matrices[-1]
    for M in reversed(matrices[:-1]):
        result = matmul(M, result)
    return result


def apply_transformation(M, points):
    """Apply matrix M to a list of (x, y) points."""
    return [mat_vec_mul(M, p) for p in points]
