import os
from pathlib import Path


def resolve_directories():
    script_dir = Path(__file__).resolve().parent
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return script_dir, output_dir


def main():
    script_dir, output_dir = resolve_directories()
    image_bytes = (script_dir / "entry_image.jpg").read_bytes()
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.png").write_bytes(image_bytes)


if __name__ == "__main__":
    main()
