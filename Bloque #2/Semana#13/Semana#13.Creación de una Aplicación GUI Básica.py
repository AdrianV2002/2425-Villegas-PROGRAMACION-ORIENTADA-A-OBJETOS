import tkinter as tk
from tkinter import messagebox


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gui | Semana#13")
        self.root.geometry("400x300")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=5)

        # Campo de texto
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Botón para agregar datos
        self.add_button = tk.Button(root, text="Agregar", command=self.add_data)
        self.add_button.pack(pady=5)

        # Lista para mostrar datos
        self.listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(pady=5)

        # Botón para limpiar datos
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_data)
        self.clear_button.pack(pady=5)

    def add_data(self):
        data = self.entry.get()
        if data:
            self.listbox.insert(tk.END, data)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo está vacío.")

    def clear_data(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un elemento para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
