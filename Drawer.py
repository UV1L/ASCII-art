from PIL import Image, ImageDraw, ImageOps, ImageFont
from termcolor import *
import RGB_Converter as rgb

CONST = 218.18181818181818182


class Drawer:

    def __init__(self, img):
        self.image_path = img
        self.img = Image.open(self.image_path)

    def resize_image(self, arg_width):

        """
        this method resize an image
        """

        width, height = self.img.size
        aspect_ratio = height / width
        new_width = arg_width
        new_height = aspect_ratio * new_width * float(arg_width) / (CONST)
        if new_height < 1:
            new_height = 1
        self.img = self.img.resize((new_width, int(new_height)))

        return new_width, new_height

    def get_image_data(self):

        """
        this method gets data from image
        """

        img = self.img.convert('L')

        pixels = img.getdata()

        return pixels

    @staticmethod
    def draw_picture(pixels):

        """
        this method draws a picture by getting its saturation from an "L"
        format
        """

        chars = [" ", ".", "'", ",", ";", ":", "c",
                 "l", "o", "d", "x", "k", "O", "0",
                 "K", "X", "N", "W", "M"]

        new_pixels = [chars[int(pixel // 14)] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        return new_pixels

    @staticmethod
    def to_ascii_art(new_pixels, new_width):

        """
        this method prints a picture from str with symbols
        """

        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in
                       range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)

        return ascii_image

    def to_ansi_art(self, _tuple):

        """
        this method draws a picture with ansi
        """

        ascii_image = _tuple[0]
        self.img = self.img.resize((_tuple[1][0], int(_tuple[1][1])))
        new_pixels = ''
        temp = 0

        for j in range(0, self.img.size[1]):
            for i in range(0, self.img.size[0]):
                rgb_symbol = rgb.get_rgb_symbol(ascii_image[temp])
                pixel = self.img.getpixel((i, j))
                if pixel == 0:
                    pixel = (0, 0, 0)
                rgb_value = rgb.get_rgb(pixel)
                new_pixels = new_pixels + colored(ascii_image[temp],
                                                  rgb_symbol,
                                                  "on_" + rgb_value,
                                                  attrs=['bold'])
                temp += 1

        new_pixels_count = len(new_pixels)
        ansi_image = [new_pixels[index:index + self.img.size[0] * 19]
                      for index in
                      range(0, new_pixels_count, self.img.size[0] * 19)]
        ansi_image = "\n".join(ansi_image)

        return ansi_image

    def get_img(self, name):

        """
        this method gets an image in .png
        """

        with open("%s.txt" % name) as text_file:
            lines = tuple(line.rstrip() for line in text_file.readlines())

        grayscale = 'L'
        font = ImageFont.truetype('cour.ttf', size=20)

        max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
        test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        max_height = self.point_to_pixel(font.getsize(test_string)[1])
        max_width = self.point_to_pixel(font.getsize(max_width_line)[0])
        height = max_height * len(lines)
        width = int(round(max_width + 40))
        image = Image.new(grayscale, (width, height), color=255)
        draw = ImageDraw.Draw(image)

        vertical_position = 5
        horizontal_position = 5
        line_spacing = int(round(max_height * 0.8))
        for line in lines:
            draw.text((horizontal_position, vertical_position),
                      line, fill=0, font=font)
            vertical_position += line_spacing

        c_box = ImageOps.invert(image).getbbox()
        image = image.crop(c_box)

        return image

    @staticmethod
    def point_to_pixel(size):
        return int(round(size * 96.0 / 72))
