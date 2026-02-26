from pathlib import Path
from PIL import Image
import hitherdither

print("Starting dithering script...")

src_dir = Path("images")
dst_dir = Path("images_dithered")
print("Looking for folder:", src_dir.resolve())

if not src_dir.exists():
    print("ERROR: _images folder not found.")
    exit(1)

dst_dir.mkdir(exist_ok=True)

palette = hitherdither.palette.Palette(
    [0x080000, 0x201A0B, 0x432817, 0x492910,
     0x234309, 0x5D4F1E, 0x9C6B20, 0xA9220F,
     0x2B347C, 0x2B7409, 0xD0CA40, 0xE8A077,
     0x6A94AB, 0xD5C4B3, 0xFCE76E, 0xFCFAE2]
)

files = list(src_dir.iterdir())
print(f"Found {len(files)} items in images")


for img_path in files:
    # only process png and gif; explicitly skip jpg/jpeg
    if img_path.suffix.lower() in (".png", "avif"):
        print("Processing:", img_path.name)
        img = Image.open(img_path)
        palette = hitherdither.palette.Palette.create_by_median_cut(img)
        img_dithered = hitherdither.ordered.bayer.bayer_dithering(
            img, palette, [256/4, 256/4, 256/4], order=8)
        out_path = dst_dir / img_path.name
        img_dithered.save(out_path)
        print("Saved:", out_path)
    else:
        print("Skipping (not processed):", img_path.name)

print("Done.")
