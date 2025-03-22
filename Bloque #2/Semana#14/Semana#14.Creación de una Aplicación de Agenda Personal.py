import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal (Adrian Villegas)")
        self.root.geometry("700x400")

        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(pady=10)

        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white',
                                     borderwidth=2)
        self.fecha_entry.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = tk.Entry(self.frame_entrada, width=30)
        self.descripcion_entry.grid(row=2, column=1)

        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=0, column=1, padx=5)

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=root.quit)
        self.btn_salir.grid(row=0, column=2, padx=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vacíos", "Todos los campos deben ser llenados")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            if messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este evento?"):
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Selección requerida", "Por favor, selecciona un evento para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
