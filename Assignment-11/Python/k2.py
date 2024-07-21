#pip install opencv-python-headless matplotlib numpy

import cv2
import matplotlib.pyplot as plt
import numpy as np

def enhance_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Could not read the image.")
        return
    

    equalized_image = cv2.equalizeHist(image)

    hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Original Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.plot(hist_original)
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.title('Equalized Image and Histogram')
    plt.imshow(equalized_image, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

    enhanced_image_path = 'enhanced_image.jpg'
    cv2.imwrite(enhanced_image_path, equalized_image)
    print(f"Enhanced image saved as '{enhanced_image_path}'")

image_path = './image.jpg'
enhance_image(image_path)

