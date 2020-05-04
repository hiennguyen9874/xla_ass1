low_frequencies = my_imfilter(image1, kernel)
high_frequencies = np.subtract(image2, my_imfilter(image2, kernel))
hybrid_image = np.add(high_frequencies, low_frequencies)
high_frequencies = np.clip(high_frequencies, 0.0, 1.0)
hybrid_image = np.clip(hybrid_image, 0.0, 1.0)