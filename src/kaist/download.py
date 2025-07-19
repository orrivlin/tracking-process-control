import os
import subprocess
from pathlib import Path

# The original KAIST download link is no longer available. The authors now
# provide the dataset via OneDrive as described here:
# https://soonminhwang.github.io/rgbt-ped-detection/
KAIST_URL = (
    "https://onedrive.live.com/download?cid=1570430EADF56512"
    "&resid=1570430EADF56512%21109419&authkey=AJcMP-7Yp86PWoE"
)
ARCHIVE_NAME = "kaist-cvpr15.tar.gz"


def download_dataset(destination: str = "data/kaist") -> Path:
    """Download the KAIST dataset to the destination directory."""
    dest = Path(destination)
    dest.mkdir(parents=True, exist_ok=True)
    archive = dest / ARCHIVE_NAME
    if not archive.exists():
        cmd = ["wget", "-O", str(archive), KAIST_URL]
        print(f"Running: {' '.join(cmd)}")
        subprocess.check_call(cmd)
    else:
        print(f"Archive {archive} already exists")
    return archive


def extract_dataset(archive: Path, destination: Path) -> None:
    """Extract the dataset if not already extracted."""
    # The archive extracts into a directory named "kaist-cvpr15".
    extract_dir = destination / "kaist-cvpr15"
    if extract_dir.exists():
        print(f"Dataset already extracted to {extract_dir}")
        return
    cmd = ["tar", "xzf", str(archive), "-C", str(destination)]
    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)


if __name__ == "__main__":
    archive_path = download_dataset()
    extract_dataset(archive_path, Path("data"))
