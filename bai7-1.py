import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class ImageBlurringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Blurring")
        
        # Tạo nút để mở bức ảnh
        open_button = tk.Button(self.root, text="Open Image", command=self.open_image)
        open_button.pack()
        
        # Tạo nút để làm mờ bức ảnh
        blur_button = tk.Button(self.root, text="Blur Image", command=self.blur_image)
        blur_button.pack()

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            if self.image is not None:
                messagebox.showinfo("Success", "Image loaded successfully")
            else:
                messagebox.showerror("Error", "Failed to load image")

    def blur_image(self):
        if hasattr(self, 'image'):
            ksize = (21, 21)
            sigma = 0
            self.image = cv2.GaussianBlur(self.image, ksize, sigma)
            cv2.imwrite('blurred_image.jpg', self.image)
            messagebox.showinfo("Success", "Image blurred and saved as 'blurred_image.jpg'")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageBlurringApp(root)
    root.mainloop()
