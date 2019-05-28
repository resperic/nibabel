anat_img = nib.load('downloads/someones_anatomy.nii.gz')
anat_img_data = anat_img.get_fdata()
anat_img_data.shape
# (57, 67, 56)
show_slices([anat_img_data[28, :, :],
             anat_img_data[:, 33, :],
             anat_img_data[:, :, 28]])
plt.suptitle("Center slices for anatomical image")  # doctest: +SKIP
