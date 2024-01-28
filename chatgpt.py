import qrcode
from PIL import Image, ImageDraw

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,
)

# Add data to the QRCode instance
data = "https://www.facebook.com"
qr.add_data(data)

# Generate the QR code
qr.make(fit=True)

# Create an image from the QRCode instance
img = qr.make_image(fill_color="black", back_color="white")

# Convert the image to RGB mode (required for Pillow)
img = img.convert('RGB')

# Create a Pillow ImageDraw object
draw = ImageDraw.Draw(img)

# Define the color for the foreground (squares) and background
foreground_color = (255, 0, 0)  # Red
background_color = (0, 0, 255)  # Blue

# Iterate through the pixels and apply the desired colors
for x in range(img.width):
    for y in range(img.height):
        pixel = img.getpixel((x, y))
        if pixel == (0, 0, 0):  # Black pixel (foreground)
            draw.point((x, y), fill=foreground_color)
        elif pixel == (255, 255, 255):  # White pixel (background)
            draw.point((x, y), fill=background_color)

# Save the colored image
img.save("fb1_colored.png")
