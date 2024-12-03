# Gaussian-filter-error-correction
### README: Correcting Images with Gaussian Filter

---

#### Project Title: Image Correction Using Gaussian Filter

---

### Description
This project demonstrates how to enhance and correct images by removing noise using a Gaussian filter. Gaussian noise is artificially added to an input image to simulate real-world noise, and the correction process is performed using the Gaussian smoothing technique. The project uses Python libraries such as `numpy`, `Pillow`, and `scipy.ndimage` for noise addition and filtering, and `matplotlib` for visualization.

---

### Features
1. Add Gaussian Noise:
   - Introduce Gaussian noise to an image based on a specified Signal-to-Noise Ratio (SNR).
2. Correct Images:
   - Apply a Gaussian filter for smoothing and noise reduction.
3. Visualization:
   - Compare the original image, noisy image, and corrected image side-by-side.

---

### Requirements
- Python 3.7+
- Libraries:
  - `numpy`
  - `Pillow`
  - `matplotlib`
  - `scipy`

Install the required dependencies using:
```bash
pip install numpy pillow matplotlib scipy
```

---

### Usage

#### 1. Load the Image
Specify the path to the input image in the code:
```python
image_path = r"C:\path\to\your\image.jpg"
original_image = np.array(Image.open(image_path))
```

#### 2. Add Gaussian Noise
Generate a noisy version of the input image by specifying the desired SNR:
```python
noisy_image = add_awgn(original_image, snr=20)
```

#### 3. Apply Gaussian Correction
Smooth the noisy image using a Gaussian filter with a specified `sigma` value:
```python
corrected_image = gaussian_correction(noisy_image, sigma=1)
```

#### 4. Visualize Results
Display the original, noisy, and corrected images for comparison:
```python
plt.subplot(1, 3, 1)  # Original image
plt.subplot(1, 3, 2)  # Noisy image
plt.subplot(1, 3, 3)  # Corrected image
plt.show()
```

---

### File Structure
- `image_correction.py`: Main script containing the noise addition, correction, and visualization functions.
- Input Image: Place your input image file at the specified path.

---

### How It Works
1. Add Gaussian Noise:
   - Noise is added to the image pixels based on the SNR value. Higher SNR values introduce less noise.
   - Noise is clipped to ensure pixel values remain within valid bounds [0, 255].

2. Gaussian Correction:
   - A Gaussian filter is applied to the noisy image to smooth out high-frequency noise.
   - The `sigma` parameter controls the strength of the filter (higher values result in more smoothing).

3. Visualization:
   - Original, noisy, and corrected images are displayed side-by-side to demonstrate the effectiveness of the correction process.

---

### Enhancements
- Adjustable SNR:
  - Modify the `snr` parameter to control the noise level.
- Dynamic Gaussian Filtering:
  - Fine-tune the `sigma` parameter to optimize the correction quality for different noise levels.
- Grayscale and RGB Support:
  - The project supports both grayscale and RGB images.

---

### Expected Results
- Noisy Image:
  - The image will have visible distortions due to Gaussian noise.
- Corrected Image:
  - Smoother and cleaner image with most of the noise removed.
