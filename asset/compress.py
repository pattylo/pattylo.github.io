import cv2

# Load the image
name = 'rip_ducky'
file_name = name + '.png'
# image = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)
image = cv2.imread(file_name)
print(image.shape)

# file_name = name + '_compressed.png'
# cv2.imwrite(file_name, image)
# print(file_name)


# Specify the scaling factor (e.g., 0.5 for half the size)
scale_percent = 50
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

# Resize the image
resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LANCZOS4)


# Save the resized image
file_name = name + '_compressed.png'
cv2.imwrite(file_name, resized_image)

print(f"Image resized to {width}x{height}")
