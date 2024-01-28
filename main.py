import qrcode

# img= qrcode.make("Hello! My name is Salil Shrestha")
# img.save("name.png")

qr= qrcode.QRCode(version=1,
                  error_correction=qrcode.ERROR_CORRECT_L,
                  box_size=20,
                  border=2)

qr.add_data("https://www.facebook.com")
qr.make(fit=True)

img1 = qr.make_image(fill_color="black", back_color="white")
img1.save("fb.png")

