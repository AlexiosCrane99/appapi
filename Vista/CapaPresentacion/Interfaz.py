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

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# Entrada de monto
label_monto = ttk.Label(frame, text="Monto:")
label_monto.grid(row=0, column=0, padx=5, pady=5)
entry_monto = ttk.Entry(frame)
entry_monto.grid(row=0, column=1, padx=5, pady=5)

# Selección de monedas
label_base = ttk.Label(frame, text="Moneda base:")
label_base.grid(row=1, column=0, padx=5, pady=5)
combo_base = ttk.Combobox(frame, values=["USD", "EUR", "GBP", "JPY", "MXN"], state="readonly")
combo_base.grid(row=1, column=1, padx=5, pady=5)
combo_base.current(0)

label_destino = ttk.Label(frame, text="Moneda destino:")
label_destino.grid(row=2, column=0, padx=5, pady=5)
combo_destino = ttk.Combobox(frame, values=["USD", "EUR", "GBP", "JPY", "MXN"], state="readonly")
combo_destino.grid(row=2, column=1, padx=5, pady=5)
combo_destino.current(1)

# Botón de conversión
btn_convertir = ttk.Button(frame, text="Convertir", command=realizar_conversion)
btn_convertir.grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta de resultado
label_resultado = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
