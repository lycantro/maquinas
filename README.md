## Cómo usar en windows:

# 🧠 HTB Machine Finder GUI

Una interfaz gráfica construida con `tkinter` para buscar y filtrar máquinas de Hack The Box desde un archivo Excel. Ideal para practicar antes de un examen de certificación y reforzar tus habilidades en pentesting.

---

## ✅ Cómo usar en Windows

### 1. **Descargar el repositorio como archivo ZIP**
Haz clic en el botón verde **"Code"** y selecciona **"Download ZIP"**.

### 2. **Descomprimir el archivo ZIP**
Extrae el contenido en una carpeta de tu preferencia (crea un archivo nuevo llamado machines).

### 3. **copia todo el contenido en machines **



### 4. **Ejecutar el archivo `maquinas.exe`**
Haz doble clic en `maquinas.exe` para iniciar la aplicación.

---

## ⚠️ Importante: Error de ruta del archivo Excel

Si al iniciar la aplicación aparece un error como:

> "No se pudo cargar el archivo Excel..."

Esto significa que el archivo `machines.xlsx` no está en la ruta esperada. 
ve a save y el archivo que se llama ruta.py abrelo en un bloc de notas y especifica la ruta donde aparece subrayado


 ## Modificar esta ruta a la tuya de machines
excel_path = os.path.expanduser("C:/Users/leona/OneDrive/Escritorio/maquinas/machines.xlsx")


