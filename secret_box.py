
from linalg import mat_vec_mul

# Column 1 = black_box(1, 0) = (0, 1)
# Column 2 = black_box(0, 1) = (-1, 0)
_SECRET_MATRIX = [
    [0, -1],
    [1, 0],
]

def black_box(point):
 
    return mat_vec_mul(_SECRET_MATRIX, point)
