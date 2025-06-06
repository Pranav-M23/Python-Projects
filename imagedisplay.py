import cv2
import matplotlib.pyplot as plt

# Read the image using OpenCV
img = cv2.imread("color_hd.jpg")

# Convert from BGR (OpenCV default) to RGB (matplotlib expects)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display using matplotlib
plt.imshow(img2)
plt.title("RCB Poster - HD")
plt.axis("off")  # Hide axes
plt.show()
