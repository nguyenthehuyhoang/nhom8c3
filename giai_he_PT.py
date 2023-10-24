import numpy as np
import tkinter as tk
from tkinter import ttk

def solve_linear_equations(coeff_matrix, constants):
    try:
        A = np.array(coeff_matrix)
        B = np.array(constants)
        A_inv = np.linalg.inv(A)
        X = np.dot(A_inv, B)
        return X
    except np.linalg.LinAlgError:
        return None

def solve_equations():
    nhapsopt = int(nhapsopt_entry.get())
    an = int(an_entry.get())
    
    hesoan_matrix = []
    hesotudo_matrix = []

    for i in range(nhapsopt):
        matrix_tam = []
        for j in range(an):
            hesoan = float(hesoan_entries[i][j].get())
            matrix_tam.append(hesoan)
        hesoan_matrix.append(matrix_tam)
        hesotudo = float(hesotudo_entries[i].get())
        hesotudo_matrix.append(hesotudo)

    nghiem = solve_linear_equations(hesoan_matrix, hesotudo_matrix)

    if nghiem is not None:
        result_label.config(text="Nghiệm của hệ phương trình:")
        for i, value in enumerate(nghiem):
            nghiem_labels[i].config(text=f"x{i+1} = {value}")
    else:
        result_label.config(text="Hệ phương trình vô nghiệm hoặc vô số nghiệm.")

root = tk.Tk()
root.title("Giải Hệ Phương Trình Tuyến Tính")

frame1 = ttk.Frame(root)
frame1.pack(padx=10, pady=10, fill='both')

nhapsopt_label = ttk.Label(frame1, text="Số lượng phương trình:")
nhapsopt_label.grid(row=0, column=0)
nhapsopt_entry = ttk.Entry(frame1)
nhapsopt_entry.grid(row=0, column=1)
nhapsopt_entry.insert(0, "2")

an_label = ttk.Label(frame1, text="Số lượng ẩn:")
an_label.grid(row=1, column=0)
an_entry = ttk.Entry(frame1)
an_entry.grid(row=1, column=1)
an_entry.insert(0, "2")

frame2 = ttk.Frame(root)
frame2.pack(padx=10, pady=10, fill='both')

hesoan_labels = []
hesotudo_labels = []

for i in range(2):
    hesoan_label = ttk.Label(frame2, text=f"Hệ số ẩn x{i+1}:")
    hesoan_label.grid(row=i, column=0)
    hesoan_labels.append(hesoan_label)

    hesotudo_label = ttk.Label(frame2, text=f"Hệ số tự do phương trình {i+1}:")
    hesotudo_label.grid(row=i, column=2)
    hesotudo_labels.append(hesotudo_label)

hesoan_entries = []
hesotudo_entries = []

for i in range(2):
    hesoan_row = []
    for j in range(2):
        hesoan_entry = ttk.Entry(frame2)
        hesoan_entry.grid(row=i, column=1)
        hesoan_row.append(hesoan_entry)
    hesoan_entries.append(hesoan_row)

    hesotudo_entry = ttk.Entry(frame2)
    hesotudo_entry.grid(row=i, column=3)
    hesotudo_entries.append(hesotudo_entry)

solve_button = ttk.Button(root, text="Giải", command=solve_equations)
solve_button.pack(pady=10)

frame3 = ttk.Frame(root)
frame3.pack(padx=10, pady=10, fill='both')

result_label = ttk.Label(frame3, text="")
result_label.grid(row=0, column=0)

nghiem_labels = []

for i in range(2):
    nghiem_label = ttk.Label(frame3, text="")
    nghiem_label.grid(row=i+1, column=0)
    nghiem_labels.append(nghiem_label)

root.mainloop()
code đúng rồi không phải sửa ạ
