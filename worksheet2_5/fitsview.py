import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.visualization import LogStretch, PercentileInterval, AsinhStretch

# open the FITS files; everything is aligned so just grab the image data directly
data_dir = "/home/shegs/Desktop/School/Astrophysics/Astro_data/MAST2_5/"
R = fits.open(data_dir + "jw01701-o031_t007_miri_f1130w-sub128_i2d.fits")[1].data
if R is None:
    print("Red channel data is empty!")
else:
    print(f"Red channel shape: {R.shape}")
    

G = fits.open(data_dir + "jw01701-o031_t007_miri_f560w-sub128_i2d.fits")[1].data
B = fits.open(data_dir + "jw01701-o031_t007_miri_f770w-sub128_i2d.fits")[1].data

# Now, these images are all weirdly rotated, so we can either rotate (requiring a SciPy call
# to do so) or we can just chop out the centre of the image.  I'm going to do that:
#R = R[2000:4000, 2000:4000]
#G = G[2000:4000, 2000:4000]
#B = B[2000:4000, 2000:4000]

crop_size = 300  # Adjust as needed
center_y, center_x = R.shape[0] // 2, R.shape[1] // 2
R = R[center_y - crop_size // 2 : center_y + crop_size // 2,
      center_x - crop_size // 2 : center_x + crop_size // 2]

G = G[center_y - crop_size // 2 : center_y + crop_size // 2,
      center_x - crop_size // 2 : center_x + crop_size // 2]

B = B[center_y - crop_size // 2 : center_y + crop_size // 2,
      center_x - crop_size // 2 : center_x + crop_size // 2]


R = np.nan_to_num(R)
G = np.nan_to_num(G)
B = np.nan_to_num(B)


# You should be frequently checking things to make sure everything looks good; let's do that now:
transform = AsinhStretch(0.03) + PercentileInterval(99.3)
fig = plt.figure()
ax = fig.add_subplot(1,3,1)
ax.imshow(transform(R), interpolation='bilinear', cmap='gray_r')
ax = fig.add_subplot(1,3,2)
ax.imshow(transform(G), interpolation='bilinear', cmap='gray_r')
ax = fig.add_subplot(1,3,3)
ax.imshow(transform(B), interpolation='bilinear', cmap='gray_r')
plt.show()

# Like I said, everything works pretty well with this, no real further tweaking required.
# So combine the three images into one RGB image -- think of it as stacking the three images on top
# of each other:

rgb = np.dstack((transform(R),transform(G),transform(B)))

# Let's take a look
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.imshow(rgb, interpolation='bilinear', origin='lower')
plt.show()

# Not bad; save it as an image
plt.imsave("m22.png", rgb, origin='lower')
