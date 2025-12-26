import customtkinter as ctk
from tkinter import filedialog
import datetime
import socket
import psutil
import os
import subprocess  # subprocess import нэмсэн

# --- Даалгавар 2: Системийн огноо цаг ---
def show_datetime():
    now = datetime.datetime.now()
    output_box.insert("end", f"Системийн огноо цаг: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

# --- Даалгавар 3: ipconfig шиг мэдээлэл ---
def show_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    output_box.insert("end", f"Төхөөрөмжийн нэр: {hostname}\n")
    output_box.insert("end", f"IP хаяг: {ip_address}\n")

    addrs = psutil.net_if_addrs()
    for iface, addr_list in addrs.items():
        output_box.insert("end", f"\nИнтерфэйс: {iface}\n")
        for addr in addr_list:
            if addr.family == socket.AF_INET:
                output_box.insert("end", f"  IP: {addr.address}\n")
                output_box.insert("end", f"  Subnet Mask: {addr.netmask}\n")
                output_box.insert("end", f"  Broadcast: {addr.broadcast}\n")
    output_box.insert("end", "\n")

# --- Даалгавар 3-аас нэмэлт: 127.0.0.1 ping ---
def ping_localhost():
    try:
        result = subprocess.check_output("ping 127.0.0.1 -n 4", shell=True, text=True, encoding="utf-8")  # Windows-д -n 4
        output_box.insert("end", "==== Ping 127.0.0.1 үр дүн ====\n")
        output_box.insert("end", result + "\n")
    except Exception as e:
        output_box.insert("end", f"Ping хийхэд алдаа гарлаа: {e}\n\n")

# --- Даалгавар 4: Batch файл шиг ажиллах ---
def run_batch_file():
    file_path = filedialog.askopenfilename(
        title="Batch файл сонгоно уу",
        filetypes=[("Text Files", "*.txt")]
    )
    if not file_path:
        return
    try:
        with open(file_path, "r") as file:
            programs = file.readlines()

        for prog in programs:
            prog = prog.strip()
            if prog:
                output_box.insert("end", f"{prog} програмыг ажиллуулж байна...\n")
                os.system(prog)
        output_box.insert("end", "\n")
    except FileNotFoundError:
        output_box.insert("end", f"{file_path} файл олдсонгүй!\n\n")

# --- UI тохиргоо ---
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("Лабораторийн ажил 4 ")
root.geometry("700x550")  # Жаахан өндөр болгосон

# Товчлуурууд
btn1 = ctk.CTkButton(root, text="Огноо цаг харуулах", command=show_datetime, width=220)
btn1.pack(pady=10)

btn2 = ctk.CTkButton(root, text="IP мэдээлэл харуулах", command=show_network_info, width=220)
btn2.pack(pady=10)

btn_ping = ctk.CTkButton(root, text="127.0.0.1 Ping хийх", command=ping_localhost, width=220)
btn_ping.pack(pady=10)

btn3 = ctk.CTkButton(root, text="Batch файл ажиллуулах", command=run_batch_file, width=220)
btn3.pack(pady=10)

# Гаралтын хэсэг
output_box = ctk.CTkTextbox(root, width=650, height=300)
output_box.pack(pady=20)

root.mainloop()
