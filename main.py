
# CORRECTING WITH GAUSSIEN FILTER
import numpy as np
from PIL import Image  # Import Image from Pillow
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def add_awgn(image, snr):
    """
    Add Gaussian noise to an image based on a given SNR (Signal-to-Noise Ratio)
    """
    image = image / 255.0  # Normalize image to [0, 1]
    noise = np.random.normal(0, 10**(-snr / 20), image.shape)  # Generate Gaussian noise
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 1)  # Clip values to valid range
    return (noisy_image * 255).astype(np.uint8)  # Rescale back to [0, 255]

def gaussian_correction(image, sigma=1):
    """
    Apply Gaussian filter for error correction
    """
    if len(image.shape) == 3:  # RGB image
        corrected_image = np.stack([gaussian_filter(image[:, :, i], sigma=sigma) for i in range(3)], axis=2)
    else:  # Grayscale image
        corrected_image = gaussian_filter(image, sigma=sigma)
    return corrected_image.astype(np.uint8)

# Load the original image
image_path = r"C:\Users\shima\OneDrive\Desktop\test\image_1.jpg"
original_image = np.array(Image.open(image_path))

# Generate the noisy image
noisy_image = add_awgn(original_image, snr=20)

# Apply Gaussian correction
corrected_image = gaussian_correction(noisy_image, sigma=1)

# Plot the original, noisy, and corrected images
plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(original_image)
plt.title("Original Image")
plt.axis('off')

# Noisy image
plt.subplot(1, 3, 2)
plt.imshow(noisy_image)
plt.title("Noisy Image")
plt.axis('off')

# Corrected image
plt.subplot(1, 3, 3)
plt.imshow(corrected_image)
plt.title("Corrected Image")
plt.axis('off')

# Show the comparison
plt.tight_layout()
plt.show()
