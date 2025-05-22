# 🧠 HTB Machine Finder GUI

Una interfaz gráfica en Tkinter para buscar máquinas de HackTheBox según dificultad, sistema operativo, tipo de examen, nombre y técnicas vistas. Incluye enlaces directos a YouTube.

---

## 🚀 ¿Cómo usar este programa?

### ✅ Paso 1: Descargar el programa

1. Descarga este repositorio como `.zip` desde GitHub.
2. Extrae el contenido en tu PC (por ejemplo, en el Escritorio).

---

### ⚠️ Paso 2: Verifica o modifica la ruta del archivo Excel

Para que el programa funcione correctamente, el archivo `machines.xlsx` **debe estar en la ruta esperada**. Por defecto, el programa busca el archivo en:

```python
C:/Users/tu_usuario/OneDrive/Escritorio/maquinas/machines.xlsx
```

🔧 Si tu usuario o ruta es diferente:

1. Abre el archivo `ruta.py` con **Notepad** o cualquier editor de texto.
2. Busca esta línea:

```python
excel_path = os.path.expanduser("C:/Users/leona/OneDrive/Escritorio/maquinas/machines.xlsx")
```

3. Modifica la ruta para que coincida con la ubicación real del archivo en tu equipo.

---

## 🖱️ Paso 3: Ejecutar el programa

### Opción A: Usar el ejecutable `.exe` (recomendado)

1. Haz doble clic en `Machines.exe`.
2. Usa los filtros para buscar máquinas.
3. Haz clic en el botón "YouTube" para abrir el writeup si está disponible.

---

### 🐍 Opción B: Ejecutar desde Python

#### Requisitos:

- Python 3.10 o superior
- Paquetes: `pandas`, `openpyxl`, `tkinter`

#### Instrucciones:

1. Abre una terminal en la carpeta `save/`.
2. Instala las dependencias:

```bash
pip install pandas openpyxl
```

3. Ejecuta el programa:

```bash
python ruta.py
```

---

## 📝 Notas adicionales

- Si el botón de YouTube no abre el enlace, revisa si hay un enlace válido en la columna correspondiente del Excel.
- Puedes crear un acceso directo al `.exe` para mayor comodidad.

---

## 🙏 Agradecimientos

Gracias a Savitar por la guía original de inspiración 🙌

---

## 🛠️ Autor

Creado por [Tu nombre o usuario de GitHub].  
Siéntete libre de hacer forks, contribuir o compartir.
