import tkinter as tk
from tkinter import ttk, messagebox
from Controlador.LogicaNegocio.Controlador import convertir_moneda

def realizar_conversion():
    try:
        monto = float(entry_monto.get())
        moneda_base = combo_base.get().upper()
        moneda_destino = combo_destino.get().upper()
        
        resultado = convertir_moneda(monto, moneda_base, moneda_destino)
        
        if resultado:
            label_resultado.config(text=f"{monto} {moneda_base} equivale a {resultado.tasa:.2f} {moneda_destino}")
        else:
            messagebox.showerror("Error", "No se pudo realizar la conversión. Verifique las monedas ingresadas.")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, ingrese un número válido para el monto.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Convertidor de Monedas")
root.geometry("400x300")
root.configure(bg="#2E2E2E")  # Fondo oscuro

# Centrar ventana en la pantalla
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (w // 2)
y = (root.winfo_screenheight() // 2) - (h // 2)
root.geometry(f"400x300+{x}+{y}")

frame = ttk.Frame(root, padding=20, style="Dark.TFrame")
frame.pack(expand=True)

# Estilos personalizados
style = ttk.Style()
style.configure("Dark.TFrame", background="#2E2E2E")
style.configure("Dark.TLabel", background="#2E2E2E", foreground="white", font=("Arial", 10))
style.configure("Dark.TButton", background="#555555", foreground="white")

# Entrada de monto
label_monto = ttk.Label(frame, text="Monto:", style="Dark.TLabel")
label_monto.grid(row=0, column=0, padx=5, pady=5)
entry_monto = ttk.Entry(frame)
entry_monto.grid(row=0, column=1, padx=5, pady=5)

# Selección de monedas
label_base = ttk.Label(frame, text="Moneda base:", style="Dark.TLabel")
label_base.grid(row=1, column=0, padx=5, pady=5)
combo_base = ttk.Combobox(frame, values=["USD", "EUR", "GBP", "COP", "MXN"], state="readonly")
combo_base.grid(row=1, column=1, padx=5, pady=5)
combo_base.current(0)

label_destino = ttk.Label(frame, text="Moneda destino:", style="Dark.TLabel")
label_destino.grid(row=2, column=0, padx=5, pady=5)
combo_destino = ttk.Combobox(frame, values=["USD", "EUR", "GBP", "COP", "MXN"], state="readonly")
combo_destino.grid(row=2, column=1, padx=5, pady=5)
combo_destino.current(1)

# Botón de conversión
btn_convertir = ttk.Button(frame, text="Convertir", command=realizar_conversion, style="Dark.TButton")
btn_convertir.grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta de resultado
label_resultado = ttk.Label(frame, text="", font=("Arial", 12, "bold"), background="#2E2E2E", foreground="white")
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
