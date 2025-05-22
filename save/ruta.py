import pandas as pd
import os
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import re
from urllib.parse import urlparse





# ######################   Modificar esta ruta a la tuya de machines   #######################
excel_path = os.path.expanduser("C:/Users/leona/OneDrive/Escritorio/maquinas/machines.xlsx")
##############################################################################################
####  ########################################################################################
####  ##############################################################  ####  ##################
####  ####### ##### #### ###### #####          #####            ####  ####  ##################
####  ######## ## ###### ###### ##### ######## ##### ###############  ##  ####################
####  ######### ######## ------ #####          ##### ###############  ##  ####################
####         ## ######## ###### ##### ######## #####            ####  ###  ###################
##############################################################################################
##############################################################################################



#########        agradecimientos a savitar por darnos  pedazo de guia      ###################














# Load Excel file
try:
    df = pd.read_excel(excel_path, sheet_name="HackTheBox", header=3)
    df = df.dropna(subset=["Máquina"])
    for col in ["Dificultad", "Sistema Operativo", "Like", "Máquina", "Writeup", "Técnicas Vistas"]:
        df[col] = df[col].fillna("").astype(str).str.strip()
    # Clean the Writeup column
    df["Writeup"] = df["Writeup"].apply(lambda x: re.sub(r'[\n\r\t]+', '', x).strip() if x else "")
    df["Writeup"] = df["Writeup"].apply(lambda x: re.sub(r'[^a-zA-Z0-9:/?=&.-]', '', x) if x else "")
    df = df.reset_index(drop=True)
    # Show first few links for debugging
    enlaces_muestra = "\n".join([f"{row['Máquina']}: {row['Writeup']}" for _, row in df.head(5).iterrows()])

except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar el archivo Excel:\n{str(e)}\n\n"
                                  "Posible causa: El archivo 'machines.xlsx' no está en el directorio especificado.\n"
                                  "Solución:\n"
                                  "1. Verifica que modificaste la ruta de tu programa en \n"
                                  "           el archivo ruta con un notepad\n"
                                  )
    exit()

resultado_actual = pd.DataFrame()
expanded_items = set()

def limpiar(texto):
    if not isinstance(texto, str):
        return ""
    return texto.lower().strip()

def validar_url(url):
    url = url.strip()
    if not url:
        return False
    try:
        parsed = urlparse(url)
        return parsed.scheme in ('http', 'https') and parsed.netloc != ''
    except Exception:
        return False

def buscar():
    global resultado_actual
    dificultad = limpiar(dificultad_var.get())
    os_filter = limpiar(os_var.get())
    examen = limpiar(examen_var.get())
    nombre = limpiar(nombre_var.get())

    resultado = df.copy()
    resultado["dificultad_norm"] = resultado["Dificultad"].apply(limpiar)
    resultado["os_norm"] = resultado["Sistema Operativo"].apply(limpiar)
    resultado["like_norm"] = resultado["Like"].apply(limpiar)
    resultado["nombre_norm"] = resultado["Máquina"].apply(limpiar)

    if dificultad:
        resultado = resultado[resultado["dificultad_norm"] == dificultad]
    if os_filter:
        resultado = resultado[resultado["os_norm"] == os_filter]
    if examen:
        resultado = resultado[resultado["like_norm"].str.contains(examen)]
    if nombre:
        resultado = resultado[resultado["nombre_norm"].str.contains(nombre)]

    resultado_actual = resultado.copy()
    actualizar_tabla(resultado)

def actualizar_tabla(data):
    tree.delete(*tree.get_children())
    for _, row in data.iterrows():
        idx = row.name
        item = tree.insert('', 'end', values=(
            "▶",
            row["Máquina"].capitalize(),
            row["Dirección IP"],
            row["Dificultad"].capitalize(),
            row["Sistema Operativo"].capitalize(),
            ", ".join(sorted(set(row["Like"].split("\n")))),
            "YouTube"
        ))
        tree.item(item, tags=(str(idx),))

def toggle_tecnicas(event):
    item = tree.identify_row(event.y)
    col = tree.identify_column(event.x)
    if not item or col != "#1":
        return
    if item in expanded_items:
        if tree.exists(f"{item}_tecnicas"):
            tree.delete(f"{item}_tecnicas")
        expanded_items.remove(item)
        tree.set(item, column="▶", value="▶")
    else:
        idx = int(tree.item(item, "tags")[0])
        tecnicas = df.at[idx, "Técnicas Vistas"]
        tree.insert(item, "end", iid=f"{item}_tecnicas", values=("", f"TÉCNICAS: {tecnicas}", "", "", "", "", ""))
        tree.item(item, open=True)
        expanded_items.add(item)
        tree.set(item, column="▶", value="▼")

def abrir_writeup(event):
    item = tree.identify_row(event.y)
    col = tree.identify_column(event.x)
    if not item or col != "#7" or "_tecnicas" in item:
        return
    try:
        idx = int(tree.item(item, "tags")[0])
        maquina = df.at[idx, "Máquina"]
        link = df.at[idx, "Writeup"].strip()
        if not link:
            messagebox.showwarning("Advertencia", f"No hay enlace de YouTube disponible para la máquina '{maquina}' (índice {idx}).")
            return
        if not validar_url(link):
            messagebox.showerror("Error", f"Enlace no válido para la máquina '{maquina}' (índice {idx}): {link}.")
            return
        messagebox.showinfo("Depuración", f"Intentando abrir enlace para la máquina '{maquina}' (índice {idx}):\n{link}")
        webbrowser.open(link)
    except Exception as e:
        error_msg = (
            f"No se pudo abrir el enlace para la máquina '{maquina}' (índice {idx}):\n{link}\n"
            f"Error: {str(e)}\n\n"
            "Posibles soluciones:\n"
            "1. asegurate de haber modificado la ruta de del archivo.\n"

        )
        messagebox.showerror("Error", error_msg)

# GUI principal
root = tk.Tk()
root.title("Maquinas")
root.geometry("1400x750")
root.configure(bg="#171a21")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview",
                font=('Segoe UI', 10, 'bold'), rowheight=36,
                background="#2a2d31", fieldbackground="#2a2d31",
                foreground="white", bordercolor="#1b2838", borderwidth=1)
style.configure("Treeview.Heading",
                font=('Segoe UI', 11, 'bold'), background="#1b2838",
                foreground="#f28f3b", relief="flat")
style.map("Treeview",
          background=[('selected', '#66c0f4')],
          foreground=[('selected', 'black')])
style.configure("Filtros.TFrame", background="#2b2f36")
style.configure("TCombobox",
                fieldbackground="#1b2838",
                background="#2b2f36",
                foreground="white",
                bordercolor="#f28f3b",
                lightcolor="#66c0f4",
                darkcolor="#171a21",
                borderwidth=2,
                relief="flat")
style.configure("TEntry",
                fieldbackground="#1b2838",
                background="#2b2f36",
                foreground="white",
                bordercolor="#f28f3b",
                lightcolor="#66c0f4",
                darkcolor="#171a21",
                borderwidth=2,
                relief="flat")
style.configure("TButton",
                background="#1b2838",
                foreground="white",
                bordercolor="#f28f3b",
                lightcolor="#66c0f4",
                darkcolor="#171a21",
                relief="flat",
                padding=8)
style.map("TButton",
          background=[('active', '#66c0f4'), ('pressed', '#f28f3b')],
          foreground=[('active', 'black'), ('pressed', 'black')])
style.configure("YouTube.TButton",
                background="#ff0000",
                foreground="white",
                font=('Segoe UI', 9, 'bold'),
                bordercolor="#ffffff",
                lightcolor="#ff5555",
                darkcolor="#cc0000",
                relief="flat",
                padding=6)
style.map("YouTube.TButton",
          background=[('active', '#ff5555'), ('pressed', '#cc0000')],
          foreground=[('active', 'white'), ('pressed', 'white')])

frame_filtros = ttk.Frame(root, padding="12", style="Filtros.TFrame")
frame_filtros.pack(fill=tk.X)

dificultad_var = tk.StringVar()
os_var = tk.StringVar()
examen_var = tk.StringVar()
nombre_var = tk.StringVar()

def crear_entrada(texto, var, fila, col, opciones=None):
    ttk.Label(frame_filtros, text=texto, background="#2b2f36", foreground="#c7d5e0", font=("Segoe UI", 10, 'bold')).grid(row=fila, column=col, sticky=tk.W, padx=4)
    if opciones:
        combo = ttk.Combobox(frame_filtros, textvariable=var, values=opciones, width=18)
        combo.grid(row=fila, column=col+1, padx=6, pady=6)
        combo.configure(style="TCombobox")
    else:
        entry = ttk.Entry(frame_filtros, textvariable=var, width=20)
        entry.grid(row=fila, column=col+1, padx=6, pady=6)
        entry.configure(style="TEntry")

crear_entrada("Dificultad:", dificultad_var, 0, 0, opciones=["", "fácil", "media", "difícil", "insane"])
crear_entrada("Sistema Operativo:", os_var, 0, 2, opciones=["", "linux", "windows"])
crear_entrada("Examen (ej. oscp):", examen_var, 0, 4)
crear_entrada("Nombre contiene:", nombre_var, 0, 6)

ttk.Button(frame_filtros, text="Buscar", command=buscar, style="TButton").grid(row=0, column=8, padx=5, pady=6)

tree = ttk.Treeview(root, columns=("▶", "Máquina", "IP", "Dificultad", "OS", "Like", "YouTube"), show="headings")
tree.heading("▶", text="▶")
tree.heading("Máquina", text="Máquina")
tree.heading("IP", text="Dirección IP")
tree.heading("Dificultad", text="Dificultad")
tree.heading("OS", text="Sistema Operativo")
tree.heading("Like", text="Like")
tree.heading("YouTube", text="YouTube")
tree.column("▶", width=50, anchor="center")
tree.column("Máquina", width=150)
tree.column("IP", width=120)
tree.column("Dificultad", width=100)
tree.column("OS", width=100)
tree.column("Like", width=200)
tree.column("YouTube", width=80, anchor="center")
tree.pack(fill=tk.BOTH, expand=True)

tree.bind("<ButtonRelease-1>", lambda e: [toggle_tecnicas(e), abrir_writeup(e)])

buscar()
root.mainloop()