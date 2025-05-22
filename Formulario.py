import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi App")

# Crear un frame con tamaño fijo
frame = tk.Frame(ventana, width=300, height=200, bg="lightgray")
frame.pack()
frame.pack_propagate(False)  # Evita que el frame se ajuste al contenido

# Etiqueta y entrada de texto dentro del frame
tk.Label(frame, text="Nombre:").pack()
entrada_nombre = tk.Entry(frame)  # CORREGIDO: nombre consistente
entrada_nombre.pack()

# Etiqueta vacía para mostrar el resultado
etiqueta_resultado = tk.Label(frame, text="", bg="lightgray")  # CORREGIDO: creada
etiqueta_resultado.pack()

# Función que se ejecuta al hacer clic en el botón
def enviar():
    nombre = entrada_nombre.get()
    mensaje = f"Hola, {nombre}!"
    etiqueta_resultado.config(text=mensaje)

# Botón para enviar el formulario
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar)
boton_enviar.pack()

ventana.mainloop()
