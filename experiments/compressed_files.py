
import PySimpleGUI as sg  # Importiert die PySimpleGUI-Bibliothek, um die GUI zu erstellen
from zip_creater import make_archive  # Importiert die Funktion make_archive aus dem Modul zip_creator

# 1. Dateiauswahl-Label und -Eingabefeld
label1 = sg.Text("Select files to compress:")  # Erstellt ein Textlabel zur Dateiauswahl
input1 = sg.Input(key="files")  # Erstellt ein Eingabefeld zur Anzeige der ausgewählten Dateien
choose_button1 = sg.FilesBrowse("Choose", key="files")  # Erstellt einen Button zur Auswahl von Dateien

# 2. Zielordner-Label und -Eingabefeld
label2 = sg.Text("Select destination folder:")  # Erstellt ein Textlabel zur Auswahl des Zielordners
input2 = sg.Input(key="folder")  # Erstellt ein Eingabefeld zur Anzeige des ausgewählten Zielordners
choose_button2 = sg.FolderBrowse("Choose", key="folder")  # Erstellt einen Button zur Auswahl des Zielordners

# 3. Komprimierungs-Button und Ausgabe-Label
compress_button = sg.Button("Compress")  # Erstellt einen Button zum Starten des Komprimierungsprozesses
output_label = sg.Text(key="output")  # Erstellt ein Textlabel zur Anzeige der Erfolgs-/Fehlermeldung

# Aufbau des Fensters mit den definierten Elementen
layout = [
    [label1, input1, choose_button1],  # Zeile 1: Dateiauswahl
    [label2, input2, choose_button2],  # Zeile 2: Zielordnerauswahl
    [compress_button, output_label]  # Zeile 3: Komprimierungs-Button und Ausgabe-Label
]

# Erstellt das Fenster mit dem Titel "File Compressor" und dem definierten Layout
window = sg.Window("File Compressor", layout)

# Event-Loop zum Anzeigen des Fensters und Verarbeiten von Benutzeraktionen
while True:
    event, values = window.read()  # Liest Ereignisse und Werte aus dem Fenster
    if event == sg.WIN_CLOSED:  # Überprüft, ob das Fenster geschlossen wurde
        break  # Bricht die Schleife ab und schließt das Fenster
    if event == "Compress":  # Überprüft, ob der Komprimierungs-Button geklickt wurde
        filepaths = values["files"].split(";")  # Holt die ausgewählten Dateipfade und trennt sie durch Semikolon
        folder = values["folder"]  # Holt den ausgewählten Zielordner
        make_archive(filepaths, folder)  # Ruft die Funktion make_archive auf, um die Dateien zu komprimieren
        window["output"].update(value="Compression completed!")  # Aktualisiert das Ausgabe-Label mit einer Erfolgsmeldung

window.close()  # Schließt das Fenster, wenn die Schleife beendet wird

