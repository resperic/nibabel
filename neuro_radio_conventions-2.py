import nibabel as nib
import matplotlib.pyplot as plt
img = nib.load('downloads/someones_anatomy.nii.gz')
# The 3x3 part of the affine is diagonal with all +ve values
img.affine
# array([[  2.75,   0.  ,   0.  , -78.  ],
# [  0.  ,   2.75,   0.  , -91.  ],
# [  0.  ,   0.  ,   2.75, -91.  ],
# [  0.  ,   0.  ,   0.  ,   1.  ]])
img_data = img.get_fdata()
a_slice = img_data[:, :, 28]
# Need transpose to put first axis left-right, second bottom-top
plt.imshow(a_slice.T, cmap="gray", origin="lower")  # doctest: +SKIP
