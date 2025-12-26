import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("💻 CPU Лабораторийн бодлогууд")
root.geometry("650x550")
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.theme_use("clam")

# Custom styles
style.configure("TNotebook.Tab", padding=[10, 5], font=("Arial", 11, "bold"))
style.configure("TButton", font=("Arial", 11, "bold"), foreground="white", background="#4CAF50")
style.map("TButton", background=[("active", "#45a049")])

# Header
header = tk.Label(root, text="CPU Лабораторийн бодлогууд", font=("Arial", 18, "bold"),
                  bg="#2196F3", fg="white", pady=10)
header.pack(fill="x")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, pady=10, padx=10)

# ------------------ Functions ------------------
def show_result(label, text):
    label.config(text=text)

def problem1():
    try:
        times = [int(x) for x in entry_p1.get().split()]
        show_result(result1, f"Хариу: {max(times)} мсек")
    except:
        show_result(result1, "❌ Алдаа: зөв тоо оруулна уу.")

def problem2():
    try:
        times = [int(x) for x in entry_p2.get().split()]
        show_result(result2, f"Хариу: {max(times)} мсек")
    except:
        show_result(result2, "❌ Алдаа: зөв тоо оруулна уу.")

def problem3():
    try:
        clock = float(entry_clock3.get())
        seq = entry_seq3.get().split()
        cpi_map = {}
        for pair in entry_cpi3.get().split(","):
            name, val = pair.strip().split("=")
            cpi_map[name.strip()] = int(val.strip())
        total_cycles = sum(cpi_map.get(inst, 0) for inst in seq)
        total_time_ns = total_cycles * clock
        show_result(result3, f"Нийт цикл: {total_cycles}\nНийт хугацаа: {total_time_ns} ns")
    except:
        show_result(result3, "❌ Алдаа: мэдээллээ шалгана уу.")

def problem4():
    try:
        clock = float(entry_clock4.get())
        seq = entry_seq4.get().split()
        cpi_map = {}
        for pair in entry_cpi4.get().split(","):
            name, val = pair.strip().split("=")
            cpi_map[name.strip()] = int(val.strip())
        total_cycles = sum(cpi_map.get(inst, 0) for inst in seq)
        total_time_ns = total_cycles * clock
        show_result(result4, f"Нийт цикл: {total_cycles}\nНийт хугацаа: {total_time_ns} ns")
    except:
        show_result(result4, "❌ Алдаа: мэдээллээ шалгана уу.")
def problem5():
    try:
        freqs = [float(x) for x in entry_freq5.get().split()]
        out = []
        for f in freqs:
            seconds = 1 / (f * 1e9)       # секунд
            nanos = seconds * 1e9         # наносекунд

            out.append(
                f"{f} ГГц процессор:\n"
                f"  1 цикл = {seconds:.3e} секунд\n"
                f"           {nanos:.4f} наносекунд\n"
               
            )
        show_result(result5, "\n\n".join(out))
    except:
        show_result(result5, "❌ Алдаа: зөв тоо оруулна уу.")

def create_tab1():
    frame = ttk.Frame(notebook)
    ttk.Label(frame, text="Програмуудын хугацаа (мсек, зайгаар тусгаарла):").pack(pady=5)
    global entry_p1, result1
    entry_p1 = ttk.Entry(frame, width=40)
    entry_p1.pack()
    ttk.Button(frame, text="Тооцоолох", command=problem1).pack(pady=5)
    result1 = tk.Message(frame, text="", bg="white", width=500, relief="solid", font=("Arial", 11))
    result1.pack(pady=5)
    return frame

def create_tab2():
    frame = ttk.Frame(notebook)
    ttk.Label(frame, text="Програмуудын хугацаа (мсек, зайгаар тусгаарла):").pack(pady=5)
    global entry_p2, result2
    entry_p2 = ttk.Entry(frame, width=40)
    entry_p2.pack()
    ttk.Button(frame, text="Тооцоолох", command=problem2).pack(pady=5)
    result2 = tk.Message(frame, text="", bg="white", width=500, relief="solid", font=("Arial", 11))
    result2.pack(pady=5)
    return frame

def create_tab3():
    frame = ttk.Frame(notebook)
    global entry_clock3, entry_cpi3, entry_seq3, result3
    ttk.Label(frame, text="Тактын хугацаа (ns):").pack()
    entry_clock3 = ttk.Entry(frame)
    entry_clock3.pack()
    ttk.Label(frame, text="CPI жагсаалт (жишээ: A=3,Б=4,В=2,Г=5):").pack()
    entry_cpi3 = ttk.Entry(frame, width=40)
    entry_cpi3.pack()
    ttk.Label(frame, text="Зааврын дараалал:").pack()
    entry_seq3 = ttk.Entry(frame, width=40)
    entry_seq3.pack()
    ttk.Button(frame, text="Тооцоолох", command=problem3).pack(pady=5)
    result3 = tk.Message(frame, text="", bg="white", width=500, relief="solid", font=("Arial", 11))
    result3.pack(pady=5)
    return frame

def create_tab4():
    frame = ttk.Frame(notebook)
    global entry_clock4, entry_cpi4, entry_seq4, result4
    ttk.Label(frame, text="Тактын хугацаа (ns):").pack()
    entry_clock4 = ttk.Entry(frame)
    entry_clock4.pack()
    ttk.Label(frame, text="CPI жагсаалт (жишээ: A=2,Б=4,В=5):").pack()
    entry_cpi4 = ttk.Entry(frame, width=40)
    entry_cpi4.pack()
    ttk.Label(frame, text="Зааврын дараалал:").pack()
    entry_seq4 = ttk.Entry(frame, width=40)
    entry_seq4.pack()
    ttk.Button(frame, text="Тооцоолох", command=problem4).pack(pady=5)
    result4 = tk.Message(frame, text="", bg="white", width=500, relief="solid", font=("Arial", 11))
    result4.pack(pady=5)
    return frame

def create_tab5():
    frame = ttk.Frame(notebook)
    global entry_freq5, result5
    ttk.Label(frame, text="Давтамж (ГГц, зайгаар тусгаарла):").pack()
    entry_freq5 = ttk.Entry(frame, width=40)
    entry_freq5.pack()
    ttk.Button(frame, text="Тооцоолох", command=problem5).pack(pady=5)
    result5 = tk.Message(frame, text="", bg="white", width=500, relief="solid", font=("Arial", 11))
    result5.pack(pady=5)
    return frame

# Add tabs
notebook.add(create_tab1(), text="1-р бодлого")
notebook.add(create_tab2(), text="2-р бодлого")
notebook.add(create_tab3(), text="3-р бодлого")
notebook.add(create_tab4(), text="4-р бодлого")
notebook.add(create_tab5(), text="5-р бодлого")

root.mainloop()
