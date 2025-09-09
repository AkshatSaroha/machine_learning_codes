import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Car_image.png')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()