import nibabel as nib
epi_img = nib.load('downloads/someones_epi.nii.gz')
epi_img_data = epi_img.get_fdata()
epi_img_data.shape
# (53, 61, 33)
