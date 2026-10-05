from pathlib import Path
# scan all files in a directory
def scan_directory(directory: Path) -> list[Path]:
    return [
        file
        for file in directory.iterdir()
        if file.is_file()
    ]