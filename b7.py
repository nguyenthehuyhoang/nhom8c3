import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                             [-1,2,2,2,-1],
                             [-1,2,8,2,-1],
                             [-1,2,2,2,-1],
                             [-1,-1,-1,-1,-1]]) / 8.0


#open image
def open_image():
    global img
    global original_img
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img = cv2.resize(img, (500, 500))  # Thay đổi kích thước thành 500x500
    original_img = img.copy()  # Lưu ảnh gốc
    cv2.imshow('Original Image', original_img)  # Hiển thị ảnh gốc

#udate
def update_sharpness_and_brightness(kernel):
    global img
    sharpness = float(sharpness_entry.get())
    brightness = float(brightness_entry.get())
    sharpened = cv2.filter2D(img, -1, kernel * sharpness)
    adjusted_brightness = cv2.convertScaleAbs(sharpened, alpha=brightness, beta=0)
    cv2.imshow('Sharpened and Brightened Image', adjusted_brightness)


root = tk.Tk()
root.title("Ứng dụng Tăng cường Sắc nét và Độ Sáng Ảnh")

btn_open = tk.Button(root, text="Chọn Ảnh", command=open_image)
btn_open.pack(pady=10)


sharpness_label = tk.Label(root, text="Sắc nét (0.1 - 5.0):")
sharpness_label.pack()
sharpness_entry = tk.Entry(root)
sharpness_entry.pack()
sharpness_entry.insert(0, "1.0")

brightness_label = tk.Label(root, text="Độ Sáng (0.1 - 5.0):")
brightness_label.pack()
brightness_entry = tk.Entry(root)
brightness_entry.pack()
brightness_entry.insert(0, "1.0")

btn_sharpen_1 = tk.Button(root, text="Kernel 1", command=lambda: update_sharpness_and_brightness(kernel_sharpen_1))
btn_sharpen_1.pack(pady=5)

btn_sharpen_2 = tk.Button(root, text="Kernel 2", command=lambda: update_sharpness_and_brightness(kernel_sharpen_2))
btn_sharpen_2.pack(pady=5)

btn_sharpen_3 = tk.Button(root, text="Kernel 3", command=lambda: update_sharpness_and_brightness(kernel_sharpen_3))
btn_sharpen_3.pack(pady=5)

root.mainloop()
