import zipfile
import pathlib

def make_archive(filepaths, dest_dir_or_zip):
    # Support string from GUI ("file1;file2") or list
    if isinstance(filepaths, str):
        filepaths = [p for p in filepaths.split(";") if p]

    dest = pathlib.Path(dest_dir_or_zip)

    # If user passed a directory, create "compressed.zip" inside it
    if not dest.suffix.lower() == ".zip":
        zip_path = dest / "compressed.zip"
    else:
        zip_path = dest

    # Ensure destination directory exists
    zip_path.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for fp in filepaths:
            p = pathlib.Path(fp)
            if p.exists():
                archive.write(p, arcname=p.name)