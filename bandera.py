from tkinter import*
# Bandera de Noruega
ventana_principal = Tk()

ventana_principal.title("Bandera de Noruega")

ventana_principal.geometry("900x500")

ventana_principal.resizable(0,0)

ventana_principal.config(bg="white")
#----------------------------------
#frames de entrada de datos

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="maroon", width=200, height=200)
frame_entrada.place(x=0, y=300)

frame_entrada1 = Frame(ventana_principal)
frame_entrada1.config(bg="maroon", width=200, height=200)
frame_entrada1.place(x=0, y=0)

frame_entrada2 = Frame(ventana_principal)
frame_entrada2.config(bg="blue4", width=1100, height=75)
frame_entrada2.place(x=0, y=212.5)

frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="blue4", width=75, height=500)
frame_resultado.place(x=212.5, y=0)


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="maroon", width=800, height=200)
frame_entrada.place(x=300, y=300)

frame_entrada1 = Frame(ventana_principal)
frame_entrada1.config(bg="maroon", width=800, height=200)
frame_entrada1.place(x=300, y=0)

ventana_principal.mainloop()
