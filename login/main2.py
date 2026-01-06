import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------
# Ventana principal
# -------------------------
root = tk.Tk()
root.title("Sistema de Aspirantes")
root.geometry("900x550")
root.configure(bg="#f4f6f8")

style = ttk.Style()
style.theme_use("default")

style.configure("TNotebook.Tab", padding=[15, 8], font=("Arial", 10, "bold"))
style.configure("TLabel", background="#f4f6f8", font=("Arial", 10))
style.configure("Title.TLabel", font=("Arial", 16, "bold"), foreground="#640174")
style.configure("TButton", font=("Arial", 10, "bold"))
style.configure("Accent.TButton", background="#3498db")

# -------------------------
# Notebook
# -------------------------
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=15, pady=15)

# =========================
# TAB 1 - DATOS BÁSICOS
# =========================
tab_basicos = ttk.Frame(notebook)
notebook.add(tab_basicos, text="Datos Básicos")

ttk.Label(tab_basicos, text="Registro del Aspirante", style="Title.TLabel")\
    .grid(row=0, column=0, columnspan=4, pady=15)

# Nombre
ttk.Label(tab_basicos, text="Nombre completo").grid(row=1, column=0, sticky="w")
entry_nombre = ttk.Entry(tab_basicos, width=30)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

# Tipo documento
ttk.Label(tab_basicos, text="Tipo de documento").grid(row=2, column=0, sticky="w")
combo_tipo_doc = ttk.Combobox(
    tab_basicos,
    values=["Cédula", "Pasaporte"],
    state="readonly",
    width=27
)
combo_tipo_doc.grid(row=2, column=1, padx=10)
combo_tipo_doc.set("Cédula")

# Número documento
ttk.Label(tab_basicos, text="Número de documento").grid(row=3, column=0, sticky="w")
entry_documento = ttk.Entry(tab_basicos, width=30)
entry_documento.grid(row=3, column=1, padx=10, pady=5)

# Teléfono
ttk.Label(tab_basicos, text="Teléfono").grid(row=4, column=0, sticky="w")
entry_telefono = ttk.Entry(tab_basicos, width=30)
entry_telefono.grid(row=4, column=1, padx=10, pady=5)

# Dirección
ttk.Label(tab_basicos, text="Dirección").grid(row=5, column=0, sticky="w")
entry_direccion = ttk.Entry(tab_basicos, width=30)
entry_direccion.grid(row=5, column=1, padx=10, pady=5)

# =========================
# TAB 2 - DATOS PERSONALES
# =========================
tab_personales = ttk.Frame(notebook)
notebook.add(tab_personales, text="Datos Personales")

ttk.Label(tab_personales, text="Información Personal", style="Title.TLabel")\
    .grid(row=0, column=0, columnspan=4, pady=15)

# Nacionalidad
ttk.Label(tab_personales, text="Nacionalidad").grid(row=1, column=0, sticky="w")
combo_nacionalidad = ttk.Combobox(
    tab_personales,
    values=["Ecuatoriana", "Colombiana", "Peruana", "Otra"],
    state="readonly"
)
combo_nacionalidad.grid(row=1, column=1, padx=10)
combo_nacionalidad.set("Ecuatoriana")

# Sexo
ttk.Label(tab_personales, text="Sexo").grid(row=2, column=0, sticky="w")
combo_sexo = ttk.Combobox(
    tab_personales,
    values=["Masculino", "Femenino", "Otro"],
    state="readonly"
)
combo_sexo.grid(row=2, column=1, padx=10)

# Estado civil
ttk.Label(tab_personales, text="Estado civil").grid(row=3, column=0, sticky="w")
combo_estado_civil = ttk.Combobox(
    tab_personales,
    values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"],
    state="readonly"
)
combo_estado_civil.grid(row=3, column=1, padx=10)

# Discapacidad
ttk.Label(tab_personales, text="¿Discapacidad?").grid(row=4, column=0, sticky="w")
combo_discapacidad = ttk.Combobox(
    tab_personales,
    values=["No", "Sí"],
    state="readonly"
)
combo_discapacidad.grid(row=4, column=1, padx=10)
combo_discapacidad.set("No")

# =========================
# TAB 3 - VIVIENDA
# =========================
tab_vivienda = ttk.Frame(notebook)
notebook.add(tab_vivienda, text="Vivienda")

ttk.Label(tab_vivienda, text="Información de Vivienda", style="Title.TLabel")\
    .grid(row=0, column=0, columnspan=4, pady=15)

ttk.Label(tab_vivienda, text="Tipo de vivienda").grid(row=1, column=0, sticky="w")
combo_tipo_vivienda = ttk.Combobox(
    tab_vivienda,
    values=["Casa", "Departamento", "Cuarto", "Otro"],
    state="readonly"
)
combo_tipo_vivienda.grid(row=1, column=1, padx=10)

ttk.Label(tab_vivienda, text="¿Internet?").grid(row=2, column=0, sticky="w")
combo_internet = ttk.Combobox(
    tab_vivienda,
    values=["Sí", "No"],
    state="readonly"
)
combo_internet.grid(row=2, column=1, padx=10)

# =========================
# TAB 4 - GUARDAR
# =========================
tab_acciones = ttk.Frame(notebook)
notebook.add(tab_acciones, text="Finalizar")

def guardar():
    if not entry_nombre.get() or not entry_documento.get():
        messagebox.showwarning("Faltan datos", "Nombre y documento son obligatorios")
        return

    messagebox.showinfo("Registro", "Información registrada correctamente")

ttk.Button(
    tab_acciones,
    text="Guardar Información",
    command=guardar
).pack(pady=50)

# -------------------------
# Loop
# -------------------------
root.mainloop()
