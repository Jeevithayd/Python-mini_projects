from PIL import Image, ImageFilter

image = Image.open(r"C:\Users\Jeevitha Y D\Pictures\photo")

# Display image
image.show()

# Convert the image to grayscale
grayscale_image = image.convert("L")
grayscale_image.show()

# Rotate the image by 90 degrees
rotated_image = image.rotate(90)
rotated_image.show()

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()

# Crop the image
cropped_image = image.crop((100, 100, 400, 400))  # Define the box (left, upper, right, lower)
cropped_image.show()

# Resize the image
resized_image = image.resize((300, 300))
resized_image.show()
# Save the manipulated image
resized_image.save("resized_example.jpg")

