import cv2
import matplotlib.pyplot as plt 

image = cv2.imread('landscape.jpg')

# check if image loaded properly
if image is None:
    print('Error: Image not found')
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    center_x, center_y = image.shape[1] // 2, image.shape[0] // 2 # 800 / 2
    #(400,400)
    crop_size = 400

    cropped_image = image[center_y - crop_size // 2: center_y + crop_size // 2,
                          center_x - crop_size // 2: center_x + crop_size // 2]
    
    plt.figure(figsize=(12,4))

    # original image
    plt.subplot(1,3,1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    # cropped image
    plt.subplot(1,3,3)
    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    plt.title('Cropped image (400 x 400 - from center)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()