
import zipfile  # Importiert das zipfile Modul, das zum Erstellen und Verwalten von ZIP-Dateien verwendet wird
import pathlib  # Importiert das pathlib Modul, das objektorientierte Pfadoperationen ermöglicht

def make_archive(filepaths, dest_dir):
    # Erstellt einen Pfad für die ZIP-Datei im Zielverzeichnis
    dest_path = pathlib.Path(dest_dir, "compressed.zip")

    # Öffnet eine neue ZIP-Datei im Schreibmodus ('w') unter dem Pfad 'dest_path'
    with zipfile.ZipFile(dest_path, 'w') as archive:
        # Iteriert über die Liste der Dateipfade
        for filepath in filepaths:
            # Fügt jede Datei zum ZIP-Archiv hinzu
            # arcname=pathlib.Path(filepath).name stellt sicher, dass nur der Dateiname und nicht der ganze Pfad ins Archiv geschrieben wird
            archive.write(filepath, arcname=pathlib.Path(filepath).name)


if __name__ == "__main__":
    # Führt die Funktion 'make_archive' aus mit den Dateipfaden ["bonus13.py", "bonus15.py"] und dem Zielverzeichnis "dest"
    make_archive(filepaths=["bonus13.py", "bonus15.py"], dest_dir="dest")

