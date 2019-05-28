# Set numpy to print 3 decimal points and suppress small values
import numpy as np
np.set_printoptions(precision=3, suppress=True)
# Print the affine
epi_img.affine
# array([[  3.   ,   0.   ,   0.   , -78.   ],
# [  0.   ,   2.866,  -0.887, -76.   ],
# [  0.   ,   0.887,   2.866, -64.   ],
# [  0.   ,   0.   ,   0.   ,   1.   ]])
