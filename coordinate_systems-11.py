import numpy.linalg as npl
epi_vox2anat_vox = npl.inv(anat_img.affine).dot(epi_img.affine)
