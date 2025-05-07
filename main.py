import tkinter as tk
from tkinter import messagebox

# Funktion zum Speichern eines Rezepts
def speichern():
    name = entry_name.get()
    zutaten = text_zutaten.get("1.0", tk.END).strip()

    if name and zutaten:
        with open("rezepte.txt", "a", encoding="utf-8") as f:
            f.write(f"Rezeptname: {name}\n")
            f.write(f"Zutaten und Zubereitung:\n{zutaten}\n")
            f.write("="*40 + "\n")
        messagebox.showinfo("Erfolg", "Rezept gespeichert!")
        entry_name.delete(0, tk.END)
        text_zutaten.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Fehler", "Bitte Name und Zutaten angeben!")

# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Küchen Rezept Manager")
fenster.geometry("400x400")

# Rezeptname
label_name = tk.Label(fenster, text="Rezeptname:")
label_name.pack()
entry_name = tk.Entry(fenster, width=50)
entry_name.pack()

# Zutaten und Zubereitung
label_zutaten = tk.Label(fenster, text="Zutaten und Zubereitung:")
label_zutaten.pack()
text_zutaten = tk.Text(fenster, height=10, width=50)
text_zutaten.pack()

# Speichern-Button
button_speichern = tk.Button(fenster, text="Speichern", command=speichern)
button_speichern.pack(pady=10)

# Tkinter-Schleife starten
fenster.mainloop()
