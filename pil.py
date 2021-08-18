from PIL import Image , ImageFilter
import matplotlib.pyplot as plt
img = Image.open("test.png")
print(img.size)
plt.imshow(img)
plt.show()