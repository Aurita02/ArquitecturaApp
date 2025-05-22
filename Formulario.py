import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi App")


frame = tk.Frame(ventana, width=300, height=200, bg="lightgray")
frame.pack()
frame.pack_propagate(False) 

tk.Label(frame, text="Nombre:").pack()
entrada_nombre = tk.Entry(frame) 
entrada_nombre.pack()

etiqueta_resultado = tk.Label(frame, text="", bg="lightgray") 
etiqueta_resultado.pack()

def enviar():
    nombre = entrada_nombre.get()
    mensaje = f"Hola, {nombre}!"
    etiqueta_resultado.config(text=mensaje)


boton_enviar = tk.Button(ventana, text="Enviar", command=enviar)
boton_enviar.pack()

ventana.mainloop()
