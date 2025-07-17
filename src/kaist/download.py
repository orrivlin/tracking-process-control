import os
import subprocess
from pathlib import Path

KAIST_URL = "http://multispectral.kaist.ac.kr/pedestrian/data-kaist.zip"


def download_dataset(destination: str = "data/kaist") -> Path:
    """Download the KAIST dataset to the destination directory."""
    dest = Path(destination)
    dest.mkdir(parents=True, exist_ok=True)
    archive = dest / "data-kaist.zip"
    if not archive.exists():
        cmd = ["wget", "-O", str(archive), KAIST_URL]
        print(f"Running: {' '.join(cmd)}")
        subprocess.check_call(cmd)
    else:
        print(f"Archive {archive} already exists")
    return archive


def extract_dataset(archive: Path, destination: Path) -> None:
    """Extract the dataset if not already extracted."""
    extract_dir = destination / "kaist"
    if extract_dir.exists():
        print(f"Dataset already extracted to {extract_dir}")
        return
    cmd = ["unzip", "-q", str(archive), "-d", str(destination)]
    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)


if __name__ == "__main__":
    archive_path = download_dataset()
    extract_dataset(archive_path, Path("data"))
