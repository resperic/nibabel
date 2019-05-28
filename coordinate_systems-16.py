cos_gamma = np.cos(0.3)
sin_gamma = np.sin(0.3)
rotation_affine = np.array([[1, 0, 0, 0],
                           [0, cos_gamma, -sin_gamma, 0],
                           [0, sin_gamma, cos_gamma, 0],
                           [0, 0, 0, 1]])
affine_so_far = rotation_affine.dot(scaling_affine)
affine_so_far
# array([[ 3.   ,  0.   ,  0.   ,  0.   ],
# [ 0.   ,  2.866, -0.887,  0.   ],
# [ 0.   ,  0.887,  2.866,  0.   ],
# [ 0.   ,  0.   ,  0.   ,  1.   ]])
