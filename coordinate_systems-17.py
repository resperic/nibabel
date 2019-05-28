translation_affine = np.array([[1, 0, 0, -78],
                               [0, 1, 0, -76],
                               [0, 0, 1, -64],
                               [0, 0, 0, 1]])
whole_affine = translation_affine.dot(affine_so_far)
whole_affine
# array([[  3.   ,   0.   ,   0.   , -78.   ],
# [  0.   ,   2.866,  -0.887, -76.   ],
# [  0.   ,   0.887,   2.866, -64.   ],
# [  0.   ,   0.   ,   0.   ,   1.   ]])
