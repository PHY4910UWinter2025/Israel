import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.visualization import LogStretch, PercentileInterval, AsinhStretch
from reproject import reproject_interp

# open the FITS files; this time we need the HDUs to reproject the images
data_dir = "/home/shegs/Desktop/School/Astrophysics/Astro_data/MAST2_5/"
hduR = fits.open(data_dir + "jw01701-o031_t007_miri_f1130w-sub128_i2d.fits")[1]
if hduR is None:
    print("Red channel data is empty!")
else:
    print(f"Red channel shape: {hduR.shape}")
    

hduG = fits.open(data_dir + "jw01701-o031_t007_miri_f560w-sub128_i2d.fits")[1]
hduB = fits.open(data_dir + "jw01701-o031_t007_miri_f770w-sub128_i2d.fits")[1]

# Here's what I mean about not being aligned; I'll stack the images using imshow and transparency
R = hduR.data
G = hduG.data
B = hduB.data

transform = AsinhStretch(0.03) + PercentileInterval(99.3)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.imshow(transform(R), interpolation='bilinear', cmap='Reds')
ax.imshow(transform(G), interpolation='bilinear', cmap='Greens', alpha=0.5)
ax.imshow(transform(B), interpolation='bilinear', cmap='Blues', alpha=0.5)
plt.show()

# okay, we'll reproject the G and R images so they match the B (the G is pretty close but has a slightly
# different resolution, so we might as well do it as well)

G, footprint = reproject_interp(hduG, hduB.header)
R, footprint = reproject_interp(hduR, hduB.header)

R = R.data
G = G.data
B = B.data


# okay we should check to see if they're okay, plot them again
transform = AsinhStretch(0.03) + PercentileInterval(99.3)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.imshow(transform(R), interpolation='bilinear', cmap='Reds')
ax.imshow(transform(G), interpolation='bilinear', cmap='Greens', alpha=0.5)
ax.imshow(transform(B), interpolation='bilinear', cmap='Blues', alpha=0.5)
plt.show()

# So, that took WAY too long to do -- once the images are aligned, we should save it and write
# another program to read it in and create the image
rgb = np.dstack((R, G, B))
if rgb is not None and rgb.size > 0:
    np.save("/home/shegs/Desktop/School/Astrophysics/worksheet2_5/ring_data.npy", rgb)
    print("ring_data.npy saved successfully!")
else:
    print("RGB data is empty. Check reprojection or data loading steps.")



