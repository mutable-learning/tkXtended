import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
from PIL.Image import Resampling


class ImageLabel(ttk.Label):

    def __init__(self, *args, image_path: str, **kwargs):
        self.image_path = image_path

        super().__init__(*args, **kwargs)
        self.update_image()

    def update_image(self):
        if self.image_path:
            self.image = ImageTk.PhotoImage(Image.open(self.image_path))
            self.config(image=self.image)

    def resize(self, width: int, height: int):
        if self.image_path:
            image_data = Image.open(self.image_path)
            image_data = image_data.resize((width, height), Resampling.LANCZOS)
            self.image = ImageTk.PhotoImage(image_data)
            self.config(image=self.image)

    def thumbnail(self, size: int):
        if self.image_path:
            thumb_data = Image.open(self.image_path)
            thumb_data.thumbnail((size, size), resample=Resampling.LANCZOS)
            self.image = ImageTk.PhotoImage(thumb_data)
            self.config(image=self.image)


if __name__ == "__main__":
    root = tk.Tk()
    image_label = ImageLabel(root, text="test label",
                             compound="bottom", image_path="",)
    image_label.pack()
    refresh_button = ttk.Button(
        root, text="Refresh", command=image_label.update_image)
    refresh_button.pack()
    thumbnail_button = ttk.Button(
        root, text="Make thumbnail", command=lambda: image_label.thumbnail(50))
    thumbnail_button.pack()
    root.mainloop()
