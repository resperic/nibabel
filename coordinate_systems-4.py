n_i, n_j, n_k = epi_img_data.shape
center_i = (n_i - 1) // 2  # // for integer division
center_j = (n_j - 1) // 2
center_k = (n_k - 1) // 2
center_i, center_j, center_k
# (26, 30, 16)
center_vox_value = epi_img_data[center_i, center_j, center_k]
center_vox_value
# 81.5492877960205...
