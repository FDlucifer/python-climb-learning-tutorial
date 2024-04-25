# pip install pillow
import os
from PIL import Image, ImageDraw, ImageFont


def add_watermark_overlay(input_image_path, output_image_path, watermark_text):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert("RGBA")
    width, height = input_image.size

    overlay = Image.new("RGBA", input_image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(overlay)

    watermark_color_pattern = (255, 255, 255, 30)

    for i in range(0, width + height, 50):
        draw.line([(0, height - i), (i, height)], fill=watermark_color_pattern, width=5)

    font_size = 80
    font = ImageFont.truetype("arial.ttf", font_size)

    text_width, text_height = draw.textsize(watermark_text, font)

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    watermark_color_text = (255, 255, 255, 80)

    draw.text((x, y), watermark_text, fill=watermark_color_text, font=font)
    watermarked_image = Image.alpha_composite(input_image, overlay)
    watermarked_image.save(output_image_path)

# input_image_path = 'car.jpg'
# output_image_path = 'car_output.jpg'
# watermark_text = "fdvoid0"

# add_watermark_overlay(input_image_path, output_image_path, watermark_text)

for file in os.listdir('images'):
    add_watermark_overlay(f'images/{file}', f'images/watermarked_{file.replace("jpg", "png")}', 'fdvoid0')
