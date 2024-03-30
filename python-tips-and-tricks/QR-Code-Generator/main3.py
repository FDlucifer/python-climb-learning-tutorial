import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("hello, i am lucifer11!", image_factory=factory)
svg_img.save("myqr.svg")