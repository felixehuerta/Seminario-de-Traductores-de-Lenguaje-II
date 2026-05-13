
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from analisis_lexico import AnalizadorLexico
from analisis_sintactico import AnalizadorSintactico
from analisis_semantico import AnalizadorSemantico


class CompiladorGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Compilador Básico de Lenguaje C")
        self.root.geometry("1200x750")

        self.crear_interfaz()

    def crear_interfaz(self):

        frame_superior = tk.Frame(self.root)
        frame_superior.pack(fill="x", padx=10, pady=5)

        btn_abrir = tk.Button(
            frame_superior,
            text="Abrir Archivo",
            command=self.abrir_archivo
        )
        btn_abrir.pack(side="left", padx=5)

        btn_compilar = tk.Button(
            frame_superior,
            text="Compilar",
            command=self.compilar_codigo
        )
        btn_compilar.pack(side="left", padx=5)

        self.editor_codigo = tk.Text(self.root, height=20, font=("Consolas", 11))
        self.editor_codigo.pack(fill="both", expand=True, padx=10, pady=10)

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_lexico = tk.Text(notebook, font=("Consolas", 10))
        self.tab_sintactico = tk.Text(notebook, font=("Consolas", 10))
        self.tab_semantico = tk.Text(notebook, font=("Consolas", 10))
        self.tab_arbol = tk.Text(notebook, font=("Consolas", 10))

        notebook.add(self.tab_lexico, text="Análisis Léxico")
        notebook.add(self.tab_sintactico, text="Análisis Sintáctico")
        notebook.add(self.tab_semantico, text="Análisis Semántico")
        notebook.add(self.tab_arbol, text="Árbol Sintáctico")

    def abrir_archivo(self):

        ruta = filedialog.askopenfilename(
            filetypes=[("Archivos C", "*.c"), ("Todos los archivos", "*.*")]
        )

        if ruta:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            self.editor_codigo.delete("1.0", tk.END)
            self.editor_codigo.insert(tk.END, contenido)

    def limpiar_tabs(self):

        self.tab_lexico.delete("1.0", tk.END)
        self.tab_sintactico.delete("1.0", tk.END)
        self.tab_semantico.delete("1.0", tk.END)
        self.tab_arbol.delete("1.0", tk.END)

    def compilar_codigo(self):

        self.limpiar_tabs()

        codigo = self.editor_codigo.get("1.0", tk.END)

        if not codigo.strip():
            messagebox.showwarning("Advertencia", "No hay código para analizar.")
            return

        try:

            # ===========================
            # ANÁLISIS LÉXICO
            # ===========================

            lexico = AnalizadorLexico()
            tokens = lexico.analizar(codigo)

            self.tab_lexico.insert(
                tk.END,
                "LEXEMA\t\tTOKEN\n"
            )
            self.tab_lexico.insert(
                tk.END,
                "-" * 50 + "\n"
            )

            for token in tokens:
                self.tab_lexico.insert(
                    tk.END,
                    f"{token['lexema']}\t\t{token['tipo']}\n"
                )

            # ===========================
            # ANÁLISIS SINTÁCTICO
            # ===========================

            sintactico = AnalizadorSintactico(tokens)
            resultado_sintactico, arbol = sintactico.analizar()

            self.tab_sintactico.insert(tk.END, resultado_sintactico)

            # ===========================
            # ANÁLISIS SEMÁNTICO
            # ===========================

            semantico = AnalizadorSemantico(tokens)
            resultado_semantico = semantico.analizar()

            self.tab_semantico.insert(tk.END, resultado_semantico)

            # ===========================
            # ÁRBOL SINTÁCTICO
            # ===========================

            self.tab_arbol.insert(tk.END, arbol)

            messagebox.showinfo(
                "Compilación Finalizada",
                "El proceso de compilación terminó correctamente."
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Ocurrió un error durante la compilación:\n\n{e}"
            )


if __name__ == "__main__":

    root = tk.Tk()
    app = CompiladorGUI(root)
    root.mainloop()
