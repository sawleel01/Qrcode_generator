import qrcode
import qrcode.image.svg

img =  qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World!", image_factory=img)
svg_img.save("myqr.svg")

