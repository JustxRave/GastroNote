import tkinter as tk
from tkinter import messagebox
import csv
import os

# Funktion zum Speichern eines Rezepts
def speichern():
    name = entry_name.get()
    zutaten = text_zutaten.get("1.0", tk.END).strip()

    if name and zutaten:
        dateiname = "rezepte.csv"
        datei_existiert = os.path.isfile(dateiname)

        with open(dateiname, mode="a", newline='', encoding="utf-8") as csvfile:
            feldnamen = ["Rezeptname", "Zutaten und Zubereitung"]
            writer = csv.DictWriter(csvfile, fieldnames=feldnamen)

            if not datei_existiert:
                writer.writeheader()

            writer.writerow({
                "Rezeptname": name,
                "Zutaten und Zubereitung": zutaten
            })

        messagebox.showinfo("Erfolg", "Rezept gespeichert!")
        entry_name.delete(0, tk.END)
        text_zutaten.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Fehler", "Bitte Name und Zutaten angeben!")

# Funktion zum Laden aller Rezepte
def laden():
    dateiname = "rezepte.csv"
    if not os.path.isfile(dateiname):
        messagebox.showinfo("Info", "Noch keine Rezepte gespeichert.")
        return

    with open(dateiname, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rezepte = ""
        for row in reader:
            rezepte += f"Rezept: {row['Rezeptname']}\n"
            rezepte += f"{row['Zutaten und Zubereitung']}\n"
            rezepte += "-" * 40 + "\n"

    text_ausgabe.delete("1.0", tk.END)
    text_ausgabe.insert(tk.END, rezepte)

# Funktion zum Suchen nach einem bestimmten Rezept
def suchen():
    suchbegriff = entry_suche.get().lower().strip()

    if not suchbegriff:
        messagebox.showwarning("Fehler", "Bitte einen Suchbegriff eingeben.")
        return

    dateiname = "rezepte.csv"
    if not os.path.isfile(dateiname):
        messagebox.showinfo("Info", "Noch keine Rezepte gespeichert.")
        return

    with open(dateiname, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        gefundene_rezepte = ""
        for row in reader:
            if suchbegriff in row['Rezeptname'].lower():
                gefundene_rezepte += f"Rezept: {row['Rezeptname']}\n"
                gefundene_rezepte += f"{row['Zutaten und Zubereitung']}\n"
                gefundene_rezepte += "-" * 40 + "\n"

    text_ausgabe.delete("1.0", tk.END)

    if gefundene_rezepte:
        text_ausgabe.insert(tk.END, gefundene_rezepte)
    else:
        text_ausgabe.insert(tk.END, "Kein passendes Rezept gefunden.")

# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Küchen Rezept Manager (Speichern + Laden + Suchen)")
fenster.geometry("700x700")

# Eingabebereich
label_name = tk.Label(fenster, text="Rezeptname:")
label_name.pack()
entry_name = tk.Entry(fenster, width=50)
entry_name.pack()

label_zutaten = tk.Label(fenster, text="Zutaten und Zubereitung:")
label_zutaten.pack()
text_zutaten = tk.Text(fenster, height=8, width=50)
text_zutaten.pack()

# Buttons zum Speichern und Laden
button_speichern = tk.Button(fenster, text="Rezept speichern", command=speichern)
button_speichern.pack(pady=5)

button_laden = tk.Button(fenster, text="Alle Rezepte laden", command=laden)
button_laden.pack(pady=5)

# Suchbereich
label_suche = tk.Label(fenster, text="Suche nach Rezeptname:")
label_suche.pack()
entry_suche = tk.Entry(fenster, width=30)
entry_suche.pack()
button_suchen = tk.Button(fenster, text="Suche starten", command=suchen)
button_suchen.pack(pady=5)

# Ausgabe-Bereich
label_ausgabe = tk.Label(fenster, text="Ergebnis:")
label_ausgabe.pack()
text_ausgabe = tk.Text(fenster, height=15, width=80)
text_ausgabe.pack()

# Tkinter-Schleife starten
fenster.mainloop()
