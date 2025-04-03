import tkinter as tk
from tkinter import messagebox

# Colores y estilos
theme_bg = "#2C3E50"
theme_fg = "#ECF0F1"
button_bg = "#3498DB"
button_fg = "#FFFFFF"
completed_task_color = "#27AE60"
font_main = ("Helvetica", 12)
font_buttons = ("Helvetica", 11, "bold")
font_title = ("Helvetica", 14, "bold")


def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")


def mark_completed(event=None):
    if root.focus_get() == task_list:
        try:
            selected_index = task_list.curselection()[0]
            task = task_list.get(selected_index)
            if not task.startswith("✔ "):
                task_list.delete(selected_index)
                task_list.insert(selected_index, "✔ " + task)
                task_list.itemconfig(selected_index, {'fg': completed_task_color})
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")


def delete_task(event=None):
    if root.focus_get() == task_list:
        try:
            selected_index = task_list.curselection()[0]
            task_list.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


def exit_app(event=None):
    root.quit()


# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("600x500")
root.configure(bg=theme_bg)
root.resizable(False, False)

# Etiqueta de título
title_label = tk.Label(root, text="Gestión de Tareas", font=font_title, fg=button_fg, bg=theme_bg)
title_label.pack(pady=10)

# Etiqueta de instrucciones
instructions_frame = tk.Frame(root, bg="#1F2C3C", padx=10, pady=10, bd=2, relief=tk.RIDGE)
instructions_frame.pack(pady=5, padx=10, fill=tk.X)
instructions_text = """Atajos de Teclado:
- Enter: Añadir tarea
- C: Marcar como completada
- D / Supr: Eliminar tarea
- Escape: Cerrar aplicación"""
instructions = tk.Label(instructions_frame, text=instructions_text, justify=tk.LEFT, font=font_main, fg=theme_fg, bg="#1F2C3C")
instructions.pack()

# Campo de entrada
task_entry = tk.Entry(root, width=50, font=font_main)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)

# Botones
button_frame = tk.Frame(root, bg=theme_bg)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Añadir", command=add_task, width=15, font=font_buttons, bg=button_bg, fg=button_fg).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Completada", command=mark_completed, width=15, font=font_buttons, bg=button_bg, fg=button_fg).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Eliminar", command=delete_task, width=15, font=font_buttons, bg=button_bg, fg=button_fg).pack(side=tk.LEFT, padx=5)

# Lista de tareas
task_list = tk.Listbox(root, width=60, height=15, selectmode=tk.SINGLE, font=font_main, bg="#34495E", fg=theme_fg)
task_list.pack(pady=10)

# Enlace de atajos de teclado
root.bind("<c>", mark_completed)
root.bind("<d>", delete_task)
root.bind("<Delete>", delete_task)
root.bind("<Escape>", exit_app)

root.mainloop()
