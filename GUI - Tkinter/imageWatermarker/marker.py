from PIL import Image, ImageDraw, ImageFont


class Marker:
    def __init__(self, file_name):
        self.filename = file_name
        self.img = Image.open(file_name)

        self.draw = ImageDraw.Draw(self.img)
        self.text = "Watermarky"
        self.font = ImageFont.truetype('times.ttf', 60)

        self.text_width, self.text_height = self.draw.textsize(self.text, self.font)
        self.width, self.height = self.img.size
        self.x_cor = self.width / 2 - self.text_width / 2
        self.y_cor = self.height - self.text_height - 350

    def create_text(self):
        self.draw.text((self.x_cor, self.y_cor), self.text, font=self.font)

    def show_image(self):
        self.img.show()


