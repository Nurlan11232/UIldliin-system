import tkinter as tk
from tkinter import messagebox

PAGE_SIZE = 1024  

# Page Table (виртуаль хуудсууд RAM дахь frame-дэй холбогдоно)
page_table = {
    0: 5,
    1: 2,
    2: 7,
    3: 1,
    4: 3,
    5: 0,
    6: 4,
    7: 6
}

# Хаягийг хөрвүүлэх функц
def translate_address():
    try:
        virtual_address = int(entry_address.get())
        page_number = virtual_address // PAGE_SIZE
        offset = virtual_address % PAGE_SIZE

        if page_number in page_table:
            frame_number = page_table[page_number]
            physical_address = frame_number * PAGE_SIZE + offset
            result_text = (
                f"Виртуаль хаяг: {virtual_address}\n"
                f"Page №: {page_number}\n"
                f"Offset: {offset}\n"
                f"Frame №: {frame_number}\n"
                f"Физик хаяг: {physical_address}"
            )
            lbl_result.config(text=result_text, fg="black")
        else:
            lbl_result.config(text=f"❌ Page {page_number} нь RAM-д байхгүй (Page Fault)", fg="red")

    except ValueError:
        messagebox.showerror("Алдаа", "Зөвхөн тоон утга оруулна уу!")

# Цонхны үндсэн тохиргоо
root = tk.Tk()
root.title("Санах ойн хаягийн хөрвүүлэлтийн симуляц (Virtual → Physical)")
root.geometry("540x480")
root.configure(bg="#e9eef5")

# Гарчиг
tk.Label(root, text="Virtual Memory Address Translation", font=("Arial", 16, "bold"), bg="#e9eef5", fg="#333").pack(pady=10)

# Хаяг оруулах хэсэг
frame_input = tk.Frame(root, bg="#e9eef5")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Виртуаль хаяг (byte): ", font=("Arial", 12), bg="#e9eef5").pack(side="left")
entry_address = tk.Entry(frame_input, width=15, font=("Arial", 12))
entry_address.pack(side="left", padx=5)

btn_translate = tk.Button(root, text="→ Хөрвүүлэх", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", command=translate_address)
btn_translate.pack(pady=10)

# Үр дүнгийн хэсэг
lbl_result = tk.Label(root, text="", font=("Consolas", 12), bg="#ffffff", width=55, height=6, relief="sunken", anchor="nw", justify="left")
lbl_result.pack(pady=10)

# Page Table-г харуулах хэсэг
tk.Label(root, text="Хуудасны хүснэгт (Page Table):", font=("Arial", 13, "bold"), bg="#e9eef5", fg="#333").pack()

table_frame = tk.Frame(root, bg="#e9eef5")
table_frame.pack(pady=5)

# Хүснэгтийн толгой
tk.Label(table_frame, text="Page №", width=10, font=("Arial", 11, "bold"), bg="#607d8b", fg="white").grid(row=0, column=0, padx=2, pady=2)
tk.Label(table_frame, text="Frame №", width=10, font=("Arial", 11, "bold"), bg="#607d8b", fg="white").grid(row=0, column=1, padx=2, pady=2)

# Хүснэгтийн мөрүүд
for i, (page, frame) in enumerate(page_table.items(), start=1):
    tk.Label(table_frame, text=page, width=10, font=("Arial", 11), bg="#f5f5f5").grid(row=i, column=0, padx=2, pady=1)
    tk.Label(table_frame, text=frame, width=10, font=("Arial", 11), bg="#f5f5f5").grid(row=i, column=1, padx=2, pady=1)

root.mainloop()
