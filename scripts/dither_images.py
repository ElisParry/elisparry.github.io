"""Simple utility to dither images under a directory.

This script walks a source tree (default `assets/images`), applies an ordered
palette dither using the `hitherdither` package, and writes the results into a
parallel directory tree specified by `--out-dir`.  It does not modify the
original files.

Usage:
    python -m scripts.dither_images --root assets/images --out-dir assets/images_dithered

The package `hitherdither` must be installed in the Python environment used to
run the script.  Install with ``pip install hitherdither``.
"""

import argparse
import sys
from pathlib import Path

from PIL import Image

try:
    import hitherdither
except ImportError:  # pragma: no cover
    print("error: hitherdither not installed", file=sys.stderr)
    sys.exit(1)

# small default palette - this can be changed if desired
PALETTE = hitherdither.palette.Palette([
    0x080000, 0x201A0B, 0x432817, 0x492910,
    0x234309, 0x5D4F1E, 0x9C6B20, 0xA9220F,
    0x2B347C, 0x2B7409, 0xD0CA40, 0xE8A077,
    0x6A94AB, 0xD5C4B3, 0xFCE76E, 0xFCFAE2
])


def process_file(src: Path, dst: Path) -> None:
    print(f"processing {src}")
    img = Image.open(src)
    dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(img, PALETTE, order=8)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dithered.save(dst)


def main() -> None:
    parser = argparse.ArgumentParser(description="Dither images recursively.")
    parser.add_argument("--root", default="assets/images", help="source directory")
    parser.add_argument("--out-dir", required=True, help="destination directory")
    args = parser.parse_args()

    root = Path(args.root)
    outroot = Path(args.out_dir)

    if not root.is_dir():
        print(f"error: source directory {root} does not exist", file=sys.stderr)
        sys.exit(1)

    for src in root.rglob("*"):
        if src.is_file() and src.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif"):
            rel = src.relative_to(root)
            dst = outroot / rel
            try:
                process_file(src, dst)
            except Exception as exc:
                print(f"error processing {src}: {exc}", file=sys.stderr)

    print("done")


if __name__ == "__main__":
    main()
