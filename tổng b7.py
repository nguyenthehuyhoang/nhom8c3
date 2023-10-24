import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# Define kernels
kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                             [-1,2,2,2,-1],
                             [-1,2,8,2,-1],
                             [-1,2,2,2,-1],
                             [-1,-1,-1,-1,-1]]) / 8.0

def open_image():
    global img
    global original_img
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img = cv2.resize(img, (500, 500))
    original_img = img.copy()
    cv2.imshow('Original Image', original_img)

def update_sharpness_and_brightness(kernel):
    global img
    sharpness = float(sharpness_entry.get())
    brightness = float(brightness_entry.get())
    sharpened = cv2.filter2D(img, -1, kernel * sharpness)
    adjusted_brightness = cv2.convertScaleAbs(sharpened, alpha=brightness, beta=0)
    cv2.imshow('Sharpened and Brightened Image', adjusted_brightness)

def blur_image():
    image = open_image()
    if image is not None:
        x, y, width, height = 100, 270, 150, 150
        roi = image[y:y+height, x:x+width]
        ksize = (21, 21)
        sigma = 0
        blurred_roi = cv2.GaussianBlur(roi, ksize, sigma)
        image[y:y+height, x:x+width] = blurred_roi
        cv2.imwrite('blurred_image.jpg', image)
        messagebox.showinfo("Success", "Image blurred and saved as 'blurred_image.jpg'")
        cv2.imshow('Original Image', image)

root = tk.Tk()
root.title("Ứng dụng Tăng cường Sắc nét, Độ Sáng và Làm Mờ Ảnh")

tab_control = ttk.Notebook(root)

tab_sharpen = ttk.Frame(tab_control)
tab_blur = ttk.Frame(tab_control)

tab_control.add(tab_sharpen, text="Tăng cường Sắc nét và Độ Sáng")
tab_control.add(tab_blur, text="Làm Mờ Ảnh")

tab_control.pack(expand=1, fill="both")

# Tab "Tăng cường Sắc nét và Độ Sáng"
btn_open = tk.Button(tab_sharpen, text="Chọn Ảnh", command=open_image)
btn_open.pack(pady=10)

sharpness_label = tk.Label(tab_sharpen, text="Sắc nét (0.1 - 5.0):")
sharpness_label.pack()
sharpness_entry = tk.Entry(tab_sharpen)
sharpness_entry.pack()
sharpness_entry.insert(0, "1.0")

brightness_label = tk.Label(tab_sharpen, text="Độ Sáng (0.1 - 5.0):")
brightness_label.pack()
brightness_entry = tk.Entry(tab_sharpen)
brightness_entry.pack()
brightness_entry.insert(0, "1.0")

btn_sharpen_1 = tk.Button(tab_sharpen, text="Kernel 1", command=lambda: update_sharpness_and_brightness(kernel_sharpen_1))
btn_sharpen_1.pack(pady=5)

btn_sharpen_2 = tk.Button(tab_sharpen, text="Kernel 2", command=lambda: update_sharpness_and_brightness(kernel_sharpen_2))
btn_sharpen_2.pack(pady=5)

btn_sharpen_3 = tk.Button(tab_sharpen, text="Kernel 3", command=lambda: update_sharpness_and_brightness(kernel_sharpen_3))
btn_sharpen_3.pack(pady=5)

# Tab "Làm Mờ Ảnh"
btn_open_blur = tk.Button(tab_blur, text="Chọn Ảnh", command=blur_image)
btn_open_blur.pack(pady=10)

root.mainloop()
