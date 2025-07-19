import os
import subprocess
from pathlib import Path

FLIR_URL = "https://flir-adas-dataset.s3.amazonaws.com/FLIR_ADAS_1_3.zip"
ARCHIVE_NAME = "FLIR_ADAS_1_3.zip"


def download_dataset(destination: str = "data/flir") -> Path:
    """Download the FLIR ADAS dataset archive."""
    dest = Path(destination)
    dest.mkdir(parents=True, exist_ok=True)
    archive = dest / ARCHIVE_NAME
    if not archive.exists():
        cmd = ["wget", "-O", str(archive), FLIR_URL]
        print(f"Running: {' '.join(cmd)}")
        subprocess.check_call(cmd)
    else:
        print(f"Archive {archive} already exists")
    return archive


def extract_dataset(archive: Path, destination: Path) -> None:
    """Extract the dataset if not already extracted."""
    extract_dir = destination / "FLIR_ADAS_1_3"
    if extract_dir.exists():
        print(f"Dataset already extracted to {extract_dir}")
        return
    cmd = ["unzip", str(archive), "-d", str(destination)]
    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)


if __name__ == "__main__":
    archive_path = download_dataset()
    extract_dataset(archive_path, Path("data"))
