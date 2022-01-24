from tkinter import *
from marker import *

BG = '#6D9886'
BUTTON_BG = '#D9CAB3'


class Setup:
    def get_image(self):
        try:
            img_path = fr"{self.entry.get()}"
            marker_obj = Marker(img_path)
            marker_obj.create_text()
            marker_obj.show_image()
            self.message.destroy()
        except:
            self.message.config(text="Invalid path!")

    def handle_click(self, event):
        self.entry.delete(0, END)

    def __init__(self):
        self.window = Tk()
        self.window.title('WaterMarky ~ Watermark your images')
        self.window.config(padx=60, pady=50, bg=BG)

        self.title_text = Label(text="WATERMARKY", font=("Courier", 15, "bold"), bg=BG)
        self.title_text.grid(row=1, column=2, columnspan=2, pady=5)

        self.entry = Entry(width=65, bg=BUTTON_BG)
        self.entry.insert(0, "Enter image path")
        self.entry.grid(row=2, column=2, columnspan=2, pady=10)
        self.entry.bind("<1>", self.handle_click)

        self.watermark_button = Button(text="Create Watermark", font=('Courier', 10, 'bold'), command=self.get_image,
                                       bg=BUTTON_BG)
        self.watermark_button.grid(row=3, column=2, columnspan=2, pady=15)

        self.message = Label(text="", font=('Courier', 10, 'bold'), bg=BG)
        self.message.grid(row=4, column=2, columnspan=2)

        self.window.mainloop()
