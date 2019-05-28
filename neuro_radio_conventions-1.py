import numpy as np
from nibabel.affines import apply_affine
diag_affine = np.array([[3., 0,  0,  0],
                        [0,  3., 0,  0],
                        [0,  0, 4.5, 0],
                        [0,  0,  0,  1]])
ijk = [1, 0, 0] # moving one unit on the first voxel axis
apply_affine(diag_affine, ijk)
# array([3., 0., 0.])
